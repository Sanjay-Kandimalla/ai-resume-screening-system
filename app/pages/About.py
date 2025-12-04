import streamlit as st
from bootstrap import *

# Page Config
st.set_page_config(page_title="About", page_icon="📘", layout="wide")

# ------------------------------------------
# ABOUT PAGE CONTENT
# ------------------------------------------

st.markdown("""
# 📘 About This Project  
### AI-Powered Resume Screening System (Capstone Project)

This application is a full **AI + NLP Resume Analyzer**, designed to simulate the 
behaviour of a modern **Applicant Tracking System (ATS)** — with deeper analysis, 
visual insights, and professional reporting.

""")

st.markdown("---")

# ----------------------------
# Core Technologies
# ----------------------------
st.markdown("""
## 🧠 Core Technologies Used  

### 🔹 Machine Learning  
- TF-IDF Vectorizer  
- Hybrid SVM Classifier  
- Category prediction  

### 🔹 Natural Language Processing (NLP)  
- Skill extraction  
- Experience & education parsing  
- Contact information detection  
- Weak/passive sentence detection  

### 🔹 Semantic Similarity (BERT)  
- Evaluates meaning-based similarity between resume & job description  

### 🔹 ATS Fit Score  
A composite score the system computes using:
- Skill match  
- TF-IDF similarity  
- BERT similarity  
- Experience match  
- Education match  

Produces a final score from **0 to 100**.

### 🔹 Visual Analytics  
- Skill gap bar charts  
- TF-IDF vs BERT similarity graphs  
- Experience comparison plots  

### 🔹 Professional ATS PDF Report  
Includes:
- Full summary  
- Match tables  
- Score bars  
- Weak writing analysis  
- Actionable recommendations  
""")

st.markdown("---")

# ----------------------------
# Project Structure
# ----------------------------
st.markdown("""
## 📁 Project Folder Structure  

```text
capstone_project/
│
├── app/
│ ├── Home.py
│ ├── bootstrap.py
│ ├── pages/
│ │ ├── Resume_Analyzer.py
│ │ ├── About.py
│ │ ├── Contact.py
│
├── data/
│
├── models/
│ ├── bert_model_name.txt
│ ├── resume_hybrid_model.pkl
│ ├── resume_model.pkl
│ ├── tfidf_vectorizer.pkl
│
├── notebooks/
│ ├── capstone project_notebook.ipynb
│
├── utils/
│ ├── fonts/
│ │ ├── DejaVuSans.ttf
│ ├── init.py
│ ├── embedding.py
│ ├── model_loader.py
│ ├── parser.py
│ ├── report.py
│ ├── scoring.py
│ ├── skills.py
│ ├── text_cleaner.py
│
├── start_app.bat
""")

st.markdown("---")

# ----------------------------
# Academic Context
# ----------------------------
st.markdown("""
## 🎓 Academic Context  

This project was developed as part of a **Master’s Capstone in Applied Statistics & Data Science**  
at the **University of Texas at Arlington**.

It demonstrates strong competencies in:

- Machine Learning  
- NLP & Text Mining  
- Software Engineering  
- Streamlit Deployment  
- Data Visualization  
- Model Evaluation & Explainability  
- End-to-end Application Design  

""")

st.success("This system showcases a complete, production-ready AI solution.")