# utils/report.py

from fpdf import FPDF
from datetime import datetime
import os
import re

# Path to your Unicode font (already downloaded)
FONT_PATH = os.path.join("utils", "fonts", "DejaVuSans.ttf")


# ------------ Helper functions ------------ #

def _split_sentences(text: str):
    """Rough sentence splitter."""
    if not text:
        return []
    text = text.replace("\n", " ")
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]


def detect_weak_sentences(resume_text: str, max_samples: int = 5):
    """
    Detect weak / passive sounding sentences using simple heuristics.
    """
    if not resume_text:
        return []

    patterns = [
        "responsible for",
        "worked on",
        "involved in",
        "helped with",
        "participated in",
        "assisted",
        "tasked with",
        "experience in",
    ]

    sentences = _split_sentences(resume_text)
    weak = []
    for s in sentences:
        low = s.lower()
        if any(p in low for p in patterns):
            weak.append(s)
        if len(weak) >= max_samples:
            break
    return weak


def add_score_bar(pdf: FPDF, label: str, score_pct: float, max_width: int = 80):
    """
    Draw a simple horizontal bar showing score (0–100%) in grayscale style.
    """
    score_pct = max(0.0, min(100.0, float(score_pct)))

    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.cell(35, 6, label, 0, 0)

    x = pdf.get_x()
    y = pdf.get_y()

    # Background bar (light grey)
    pdf.set_draw_color(200, 200, 200)
    pdf.set_fill_color(235, 235, 235)
    pdf.rect(x, y + 2, max_width, 4, style="F")

    # Filled portion (dark grey)
    fill_width = max_width * (score_pct / 100.0)
    pdf.set_fill_color(80, 80, 80)
    pdf.rect(x, y + 2, fill_width, 4, style="F")

    # Percentage text
    pdf.set_xy(x + max_width + 3, y)
    pdf.cell(0, 6, f"{round(score_pct, 1)}%", 0, 1)


# ------------ PDF Class ------------ #

class ATSReportPDF(FPDF):

    def header(self):
        # Title block
        self.set_font("DejaVu", "B", 18)
        self.set_text_color(20, 20, 20)
        self.cell(0, 10, "AI-Powered ATS Resume Report", ln=True, align="C")

        self.set_font("DejaVu", "", 10)
        self.set_text_color(90, 90, 90)
        self.cell(0, 6,
                  f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                  ln=True, align="C")

        # Thin grey line separator
        self.ln(3)
        self.set_draw_color(180, 180, 180)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        # Position 15 mm from bottom
        self.set_y(-15)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())

        self.set_font("DejaVu", "", 8)
        self.set_text_color(120, 120, 120)
        # Left side: branding
        self.cell(0, 5, "AI-Powered Resume Screening System", align="L")
        # Right side: page number
        self.set_y(self.get_y())
        self.cell(0, 5, f"Page {self.page_no()}", align="R")

    def section_title(self, title):
        # Section header with light grey background
        self.ln(4)
        self.set_fill_color(235, 235, 235)
        self.set_draw_color(200, 200, 200)
        self.set_text_color(20, 20, 20)
        self.set_font("DejaVu", "B", 13)

        self.cell(0, 8, f"  {title}", ln=True, fill=True, border=1)
        self.ln(2)

    def subsection_title(self, title):
        self.set_font("DejaVu", "B", 11)
        self.set_text_color(40, 40, 40)
        self.ln(1)
        self.cell(0, 6, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_text(self, text):
        self.set_font("DejaVu", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5, text)
        self.ln(1)


# ------------ Main entry: create_ats_report ------------ #

def create_ats_report(
    final_score,
    skill_match_percent,
    bert_score,
    tfidf_sim,
    exp_score,
    edu_score,
    experience_years,
    education_level,
    resume_skills,
    jd_skills,
    missing_skills,
    predicted_category,
    model_confidence,
    contact_info,
    resume_text,
):
    pdf = ATSReportPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Register Unicode font
    pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
    pdf.add_font("DejaVu", "B", FONT_PATH, uni=True)

    # ---------------------- COVER-STYLE FIRST PAGE ---------------------- #
    pdf.add_page()

    # Top “summary card”
    pdf.section_title("Overall ATS Summary")

    skill_pct = float(skill_match_percent)
    tfidf_pct = float(tfidf_sim) * 100.0
    bert_pct = float(bert_score) * 100.0
    exp_pct = float(exp_score) * 100.0
    edu_pct = float(edu_score) * 100.0

    # Big ATS Score Highlight
    pdf.set_font("DejaVu", "B", 24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 12, f"ATS Fit Score: {round(final_score, 1)}%", ln=True, align="L")
    pdf.ln(2)

    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(
        0,
        5,
        "This score summarizes how well your resume aligns with the target job "
        "based on skills, text similarity (TF-IDF & BERT), experience, and education."
    )

    # Quick metrics summary in two columns
    pdf.ln(2)
    pdf.set_font("DejaVu", "", 10)
    pdf.set_text_color(30, 30, 30)

    pdf.cell(60, 6, f"• Skill Match: {round(skill_pct, 1)}%", ln=False)
    pdf.cell(0, 6, f"• TF-IDF Similarity: {round(tfidf_pct, 1)}%", ln=True)
    pdf.cell(60, 6, f"• BERT Similarity: {round(bert_pct, 1)}%", ln=False)
    pdf.cell(0, 6, f"• Experience Match: {round(exp_pct, 1)}%", ln=True)
    pdf.cell(60, 6, f"• Education Match: {round(edu_pct, 1)}%", ln=True)

    # ---------------------- ATS Match Summary Table ---------------------- #
    pdf.section_title("ATS Match Summary Table")

    pdf.set_font("DejaVu", "B", 10)
    pdf.set_fill_color(240, 240, 240)
    pdf.set_draw_color(200, 200, 200)
    pdf.cell(70, 7, "Metric", border=1, align="L", fill=True)
    pdf.cell(30, 7, "Score (%)", border=1, align="C", fill=True)
    pdf.ln()

    pdf.set_font("DejaVu", "", 10)
    rows = [
        ("Skill Match", skill_pct),
        ("TF-IDF Similarity", tfidf_pct),
        ("BERT Similarity", bert_pct),
        ("Experience Match", exp_pct),
        ("Education Match", edu_pct),
    ]
    for label, val in rows:
        pdf.cell(70, 7, label, border=1)
        pdf.cell(30, 7, f"{round(val, 1)}", border=1, align="C")
        pdf.ln()

    # ---------------------- Visual Score Bars ---------------------- #
    pdf.section_title("Visual Match Scores")
    add_score_bar(pdf, "Skill Match", skill_pct)
    add_score_bar(pdf, "TF-IDF", tfidf_pct)
    add_score_bar(pdf, "BERT", bert_pct)
    add_score_bar(pdf, "Experience", exp_pct)
    add_score_bar(pdf, "Education", edu_pct)

    # ---------------------- Contact Info ---------------------- #
    pdf.section_title("Candidate Contact Information")
    pdf.subsection_title("Detected Contact Details")
    contact_txt = (
        f"Email: {contact_info.get('email') or 'Not detected'}\n"
        f"Phone: {contact_info.get('phone') or 'Not detected'}"
    )
    pdf.section_text(contact_txt)

    # ---------------------- Experience & Education ---------------------- #
    pdf.section_title("Experience & Education Alignment")
    exp_edu = (
        f"Years of Experience (detected): {experience_years}\n"
        f"Highest Education Level: {education_level}\n\n"
        f"Experience Match Score: {round(exp_pct, 1)}%\n"
        f"Education Match Score: {round(edu_pct, 1)}%"
    )
    pdf.section_text(exp_edu)

    # ---------------------- Model Output + Explanation ---------------------- #
    pdf.section_title("Model Classification Output")

    model_txt = (
        f"Predicted Resume Category: {predicted_category}\n"
        f"Hybrid Model Confidence (raw): {round(model_confidence, 2)}"
    )
    pdf.section_text(model_txt)

    # Simple “Why this category?” explanation
    resume_skills = resume_skills or []
    jd_skills = jd_skills or []

    if jd_skills:
        matched_keywords = sorted(set(resume_skills) & set(jd_skills))
    else:
        matched_keywords = sorted(set(resume_skills))

    pdf.subsection_title("Why This Category Was Predicted")
    if matched_keywords:
        top_kw = ", ".join(matched_keywords[:12])
        why_txt = (
            "The model likely selected this category because your resume "
            "emphasizes skills and keywords such as:\n"
            f"{top_kw}."
        )
    else:
        why_txt = (
            "The model relied on general text patterns (roles, titles, and "
            "technical language) in your resume to classify it into this category."
        )
    pdf.section_text(why_txt)

    # ---------------------- Skills Analysis ---------------------- #
    pdf.section_title("Skills Analysis")

    resume_skills_txt = ", ".join(sorted(resume_skills)) if resume_skills else "None detected"
    jd_skills_txt = ", ".join(sorted(jd_skills)) if jd_skills else "None detected"
    missing_txt = (
        ", ".join(sorted(missing_skills))
        if missing_skills
        else "None (all required skills present)"
    )

    pdf.subsection_title("Skills Found in Resume")
    pdf.section_text(resume_skills_txt)

    pdf.subsection_title("Skills Required in Job Description")
    pdf.section_text(jd_skills_txt)

    pdf.subsection_title("Missing or Underrepresented Skills")
    pdf.section_text(missing_txt)

    # ---------------------- Similarity Scores ---------------------- #
    pdf.section_title("Text Similarity Scores")

    sim_text = (
        f"TF-IDF Similarity (keyword-based): {round(tfidf_pct, 1)}%\n"
        f"BERT Semantic Similarity (context-based): {round(bert_pct, 1)}%"
    )
    pdf.section_text(sim_text)

    # ---------------------- Weak Sentence Detection ---------------------- #
    pdf.section_title("Writing Quality – Weak / Passive Sentences")

    weak_sents = detect_weak_sentences(resume_text, max_samples=5)

    if weak_sents:
        weak_block = "These sentences could be made more action-oriented and impactful:\n\n"
        for i, s in enumerate(weak_sents, start=1):
            weak_block += f"{i}. {s}\n\n"
        weak_block += (
            "Try rewriting using strong action verbs (Led, Designed, Built, "
            "Improved by X%, Automated, Optimized, etc.) and quantifiable results."
        )
    else:
        weak_block = (
            "No clearly weak or passive sentences were detected using our simple rules.\n"
            "Your bullet points already appear action-focused."
        )
    pdf.section_text(weak_block)

    # ---------------------- High-Level Recommendations ---------------------- #
    pdf.section_title("High-Level Recommendations")

    rec_list = []
    if missing_skills:
        rec_list.append(
            "• Highlight or learn the missing skills mentioned in the job description where possible."
        )
    if exp_score < 1.0:
        rec_list.append(
            "• Your experience appears below the typical requirement; emphasize impact, projects, "
            "and measurable outcomes from your work."
        )
    if edu_score < 1.0:
        rec_list.append(
            "• Your education level may be below the preferred level; focus on certifications, "
            "practical projects, and specialized courses."
        )
    if not rec_list:
        rec_list.append(
            "• Your profile is a strong match. Continue refining your summary, add measurable results, "
            "and tailor the resume for each application."
        )

    pdf.section_text("\n".join(rec_list))

    # Return raw bytes (works with Streamlit download_button)
    pdf_bytes = pdf.output(dest="S")
    return bytes(pdf_bytes)