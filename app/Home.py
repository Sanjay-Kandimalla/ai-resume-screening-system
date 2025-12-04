import streamlit as st
from bootstrap import *

# Configure Home page
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🏠",
    layout="wide"
)


# ------------------------------
# Home Page Content
# ------------------------------

st.markdown("""
# 🏠 AI-Powered Resume Screening System  
### Your Personal ATS — Powered by Machine Learning + NLP  
""")

st.write("""
Welcome to a **full-scale AI Resume Analyzer** that evaluates resumes 
the same way modern **Applicant Tracking Systems (ATS)** do — and goes beyond.

This platform combines:

- ✔ Machine Learning Classification  
- ✔ NLP Skill Extraction  
- ✔ Semantic Similarity (BERT)  
- ✔ Resume–JD Matching  
- ✔ ATS Fit Score (0–100)  
- ✔ Professional PDF Report Generation  
""")

# ---------------- IMAGE ----------------
st.image(
    "https://cdn-icons-png.flaticon.com/512/4727/4727424.png",
    width=230
)

# ---------------- FEATURES ----------------
st.markdown("""
---

## 🚀 What You Can Do Here

### 🔍 1. Analyze Your Resume  
Upload a **PDF or DOCX** file or paste raw text.

### 📌 2. Extract Skills & Experience  
Automatically detects:
- Technical & soft skills  
- Experience years  
- Education level  
- Contact details  

### 🎯 3. Compare Resume with Job Description  
Get:
- Skill Match Percentage  
- TF-IDF Similarity  
- BERT Semantic Similarity  
- Missing Skills  

### ⭐ 4. ATS Fit Score (0–100)  
Calculated from:
- Skills Match  
- Semantic Similarity  
- Experience  
- Education  

### 📊 5. Visual Analytics  
Includes:
- Skill match bar chart  
- TF-IDF vs BERT similarity chart  
- Experience comparison plot  

### 📄 6. Download Premium ATS PDF Report  
Includes:
- Full breakdown  
- Weak sentence detection  
- Category prediction explanation  
- Actionable recommendations  

---

## 🧭 Get Started
Use the **sidebar on the left** to navigate.

👉 Click **🧠 Resume Analyzer** to begin.
""")