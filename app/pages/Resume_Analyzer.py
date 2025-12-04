# ==========================================================
# AI-Powered Resume Screening System - Streamlit App (Hybrid)
# ==========================================================

import sys
import os
from bootstrap import *   # DO NOT REMOVE — required for path fixing

# Absolute project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
import joblib, re, nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.graph_objects as go

# === Custom Utility Imports ===
from utils.parser import extract_text_from_upload, extract_contact_details, extract_experience_years, extract_education_level
from utils.skills import extract_skills
from utils.embedding import compute_bert_similarity
from utils.scoring import score_experience, score_education, final_ats_score
from utils.report import create_ats_report

# Initialize dynamic uploader key
if "uploader_key" not in st.session_state:
    st.session_state["uploader_key"] = "resume_uploader_1"


# ----------------------------------------------------------
# Load Required Artifacts (Hybrid Model + TF-IDF)
# ----------------------------------------------------------
@st.cache_resource
def load_models():
    tfidf = joblib.load("models/tfidf_vectorizer.pkl")
    hybrid_model = joblib.load("models/resume_hybrid_model.pkl")  # NEW
    bert = SentenceTransformer("all-MiniLM-L6-v2")                # NEW
    return tfidf, hybrid_model, bert

tfidf, hybrid_model, bert_model = load_models()


# ----------------------------------------------------------
# NLTK Setup
# ----------------------------------------------------------
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

_stop = set(stopwords.words("english"))
_lem = WordNetLemmatizer()

def clean_text(text: str) -> str:
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    tokens = [_lem.lemmatize(w) for w in text.split() if w not in _stop]
    return " ".join(tokens)


# ----------------------------------------------------------
#                    STREAMLIT UI
# ----------------------------------------------------------
st.markdown("""
# AI-Powered Resume Screening System  
### Hybrid Model (BERT + TF-IDF) Powered ATS Analyzer
""")

st.write("Upload your resume or paste text below.")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"], key=st.session_state["uploader_key"])
if uploaded_file is not None:
    if st.button("Remove Uploaded File"):
        # Assign a brand new widget key → this forces Streamlit to reset the uploader
        st.session_state["uploader_key"] = f"resume_uploader_{os.urandom(4)}"
        st.rerun()

resume_text = st.text_area("Or paste resume text:", height=220)
job_description = st.text_area("Paste Job Description (Optional)", height=160)


# ----------------------------------------------------------
#                  PROCESS PIPELINE
# ----------------------------------------------------------
if st.button("Analyze Resume"):

    # 1️⃣ Extract Text
    if uploaded_file:
        raw_resume_text = extract_text_from_upload(uploaded_file)
    elif resume_text.strip():
        raw_resume_text = resume_text
    else:
        st.warning("Please upload a resume or paste text.")
        st.stop()

    # 2️⃣ Contact Info
    contact_info = extract_contact_details(raw_resume_text)

    # 3️⃣ Skills
    resume_skills = extract_skills(raw_resume_text)

    # 4️⃣ Experience + Education
    experience_years = extract_experience_years(raw_resume_text)
    education_level = extract_education_level(raw_resume_text)

    # ----------------------------------------------------------
    #         HYBRID PREDICTION (BERT + TF-IDF)
    # ----------------------------------------------------------
    with st.spinner("Running Hybrid Model (BERT + TF-IDF)..."):

        cleaned = clean_text(raw_resume_text)

        # --- TF-IDF vector ---
        tfidf_vec = tfidf.transform([cleaned]).toarray()

        # --- BERT vector ---
        bert_vec = bert_model.encode([raw_resume_text])

        # --- HYBRID FEATURE = CONCAT(BERT, TF-IDF) ---
        hybrid_vec = np.hstack((bert_vec, tfidf_vec))

        pred = hybrid_model.predict(hybrid_vec)[0]

        # Confidence: cosine similarity to training support vectors
        decision_val = hybrid_model.decision_function(hybrid_vec)
        hybrid_conf = float(np.max(decision_val))


    # ----------------------------------------------------------
    #               DISPLAY PREDICTION RESULTS
    # ----------------------------------------------------------
    st.success(f"Predicted Category: **{pred}**")
    st.info(f"Hybrid Model Confidence: **{hybrid_conf:.2f}**")


    # Contact Info
    with st.expander("📬 Contact Info"):
        st.write(contact_info)

    # Skills
    with st.expander("🛠 Skills Detected in Resume"):
        st.write(", ".join(resume_skills) if resume_skills else "No skills detected")

    # Experience/Education
    with st.expander("🎓 Experience & Education"):
        st.write(f"**Years of Experience:** {experience_years}")
        st.write(f"**Education Level:** {education_level}")


    # ----------------------------------------------------------
    #                  JD ANALYSIS + MATCHING
    # ----------------------------------------------------------
    if job_description.strip():

        jd_skills = extract_skills(job_description)
        matched = len(set(resume_skills) & set(jd_skills))
        total = len(jd_skills)
        skill_match_percent = round((matched / total) * 100, 2) if total else 0
        st.metric("Skill Match %", f"{skill_match_percent}%")
        


        # TF-IDF Similarity
        jd_clean = clean_text(job_description)
        jd_vec = tfidf.transform([jd_clean])
        tfidf_sim = float(cosine_similarity(tfidf_vec, jd_vec)[0][0])

        # BERT Similarity
        bert_score = compute_bert_similarity(raw_resume_text, job_description)

        st.metric("TF-IDF Similarity", f"{round(tfidf_sim * 100, 2)}%")
        st.metric("BERT Similarity", f"{round(bert_score * 100, 2)}%")


        # Final ATS Score
        exp_score = score_experience(experience_years, job_description)
        edu_score = score_education(education_level, job_description)

        final_score = final_ats_score(
            skill_match_percent/100, bert_score, tfidf_sim, exp_score, edu_score
        )

        st.markdown(f"## ⭐ Final ATS Score: **{final_score}%**")


        # Missing Skills
        missing_skills = set(jd_skills) - set(resume_skills)
        with st.expander("❌ Missing Skills"):
            st.write(", ".join(missing_skills) if missing_skills else "No missing skills!")


        # ------------------------------------------------------
        #       PDF REPORT DOWNLOAD
        # ------------------------------------------------------
        report_bytes = create_ats_report(
            final_score=final_score,
            skill_match_percent=skill_match_percent,
            bert_score=bert_score,
            tfidf_sim=tfidf_sim,
            exp_score=exp_score,
            edu_score=edu_score,
            experience_years=experience_years,
            education_level=education_level,
            resume_skills=resume_skills,
            resume_text=raw_resume_text,
            jd_skills=jd_skills,
            missing_skills=missing_skills,
            predicted_category=pred,
            model_confidence= hybrid_conf,
            contact_info=contact_info,
        )

        st.download_button(
            label="📄 Download ATS Report",
            data=report_bytes,
            file_name="ATS_Resume_Report.pdf",
            mime="application/pdf",
        )