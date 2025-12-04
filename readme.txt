<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/4727/4727424.png" width="130"/>
</p>

<h1 align="center">AI-Powered Resume Screening System</h1>

<p align="center">
  A complete Machine Learning + NLP system that analyzes resumes like a modern ATS,
  evaluates job-fit using hybrid similarity models, and generates a PDF insights report.
</p>

---

## 🚀 Overview

This project is an end-to-end **AI Resume Analyzer** that helps automate resume–job description matching by combining **ML classification**, **semantic similarity**, and **rule-based skill extraction**.

The system:

- Extracts skills, experience, education & contact info  
- Predicts resume category using **SVM + TF-IDF**  
- Computes semantic similarity using **Sentence-BERT**  
- Calculates keyword similarity using **TF-IDF cosine similarity**  
- Generates **Hybrid ATS Fit Score** (0–100)  
- Produces a **professional PDF Report**  
- Runs fully as a **Streamlit Web App**  

---

## ✨ Key Features

### 📄 Resume Parsing
- Extracts email, phone, education level, experience years  
- Reads **PDF, DOCX, TXT**  
- Standardizes text using advanced cleaning pipeline  

### 🤖 AI + NLP Components
- **TF-IDF + Linear SVM** for resume category classification  
- **Sentence-BERT** (SBERT) for semantic similarity  
- **Rule-based NLP** for skill extraction  
- Weak/passive sentence detection  

### 📊 Analytics & Scoring
- Keyword Match Score (TF-IDF)  
- Semantic Similarity Score (BERT)  
- Skill Match Percentage  
- Category Prediction Confidence  
- Hybrid ATS Fit Score (0–100)  

### 📄 Automated PDF Report
(Generated using ReportLab / custom layout)

Includes:
- Summary table  
- Visual scoring bars  
- Missing skills  
- Weak sentence highlights  
- Final ATS Fit Recommendations  

---

## 🧠 Tech Stack

| Category | Tools / Libraries |
|----------|-------------------|
| **Language** | Python |
| **Web App** | Streamlit |
| **ML / NLP** | Scikit-learn, Sentence-BERT |
| **Parsing** | Regex-based rules |
| **Embeddings** | SBERT (sentence-transformers) |
| **Reports** | ReportLab |
| **Visualization** | Plotly / Matplotlib |
| **Packaging** | Requirements.txt |

---

## 🗂 Project Structure
capstone_project/
│
├── app/
│   ├── Home.py
│   ├── bootstrap.py
│   ├── pages/
│       ├── Resume_Analyzer.py
│       ├── About.py
│       ├── Contact.py
│
├── utils/
│   ├── parser.py
│   ├── skills.py
│   ├── scoring.py
│   ├── embedding.py
│   ├── report.py
│   ├── text_cleaner.py
│   ├── fonts/DejaVuSans.ttf
│
├── models/
│   ├── tfidf_vectorizer.pkl
│   ├── resume_model.pkl
│   ├── resume_hybrid_model.pkl
│   ├── bert_model_name.txt
│
├── data/
├── notebooks/
├── start_app.bat
│
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sanjay-Kandimalla/ai-resume-screening-system.git
cd ai-resume-screening-system
________________________________________
🧪 Running the Notebook
The notebooks/ folder contains:
•	Data exploration
•	Model training
•	Feature engineering
•	BERT embedding testing


2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app/Home.py

4️⃣ Open in Browser
http://localhost:8501

🧪 Jupyter Notebooks

The notebooks/ folder includes:

Data exploration

Model training

TF-IDF / SVM experiments

BERT embedding experiments

Hybrid scoring research
________________________________________
📄 PDF ATS Report Generation

After uploading a resume & pasting a job description:

System computes all similarity + ML scores

Generates improvement insights

Click Generate Report

A professional PDF downloads automatically
________________________________________
✍️ Author

Sanjay Kandimalla
Master’s in Applied Statistics & Data Science
University of Texas at Arlington
📧 sanjay.kandimalla2025@gmail.com

📍 Arlington, TX
🔗 LinkedIn: https://www.linkedin.com/in/sanjay-kandimalla/

🔗 GitHub: https://github.com/Sanjay-Kandimalla
________________________________________
⭐ License

This project is open for academic use, learning, and portfolio demonstration.
Commercial reuse is not permitted.

