📄 README.md — AI-Powered Resume Screening System
<p align="center"> <img src="https://cdn-icons-png.flaticon.com/512/4727/4727424.png" width="140"/> </p> <h1 align="center">AI-Powered Resume Screening System</h1> <p align="center"> A full-scale Machine Learning + NLP system that evaluates resumes like a modern ATS and generates a professional PDF analysis report. </p> 
________________________________________
🚀 Overview
This project is a complete AI Resume Analyzer that:
•	Extracts skills, experience, education & contact info
•	Matches resumes with job descriptions
•	Calculates semantic similarity using BERT
•	Predicts resume category using SVM + TF-IDF
•	Generates a Final ATS Fit Score
•	Creates a premium PDF Report with insights
•	Runs as a Streamlit web application
________________________________________
✨ Key Features
📄 Resume Parsing
•	Extracts phone, email, education, years of experience, and skills
•	Supports PDF, DOCX, and raw text
🤖 AI/ML Components
•	TF-IDF + SVM classifier for resume category prediction
•	Hybrid semantic similarity using Sentence-BERT
•	Skill extraction using rule-based NLP patterns
•	Weak sentence detection for writing improvement
📊 Analytics & Scoring
•	Skill Match %
•	TF-IDF Similarity
•	BERT Semantic Similarity
•	Experience/Education Match
•	Final ATS Fit Score (0–100)
📄 Premium PDF Report (FPDF2)
Includes:
•	ATS summary table
•	Visual score bars
•	Weak/passive sentence detection
•	Missing skills
•	Recommendations
________________________________________
🧠 Tech Stack
Category	Tools / Libraries
Language	Python
Web App	Streamlit
ML/NLP	Scikit-learn, Sentence-BERT
Parsing	SpaCy-like regex patterns
Visuals	Plotly
Reports	FPDF2
Packaging	Pip + Requirements.txt
________________________________________
🗂 Project Structure
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
________________________________________
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/resume-ats-analyzer.git
cd resume-ats-analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit App
streamlit run app/Home.py
4️⃣ Visit in Browser
http://localhost:8501
________________________________________
🧪 Running the Notebook
The notebooks/ folder contains:
•	Data exploration
•	Model training
•	Feature engineering
•	BERT embedding testing
________________________________________
📄 Generating PDF ATS Reports
Inside the app, after analyzing a resume:
•	Click Generate Report
•	Download your personalized PDF
________________________________________
✍️ Author
Sanjay Kandimalla
Master’s in Applied Statistics & Data Science
University of Texas at Arlington
📧 sanjay.kandimalla2025@gmail.com
📍 Arlington, TX
🔗 LinkedIn: https://www.linkedin.com/in/sanjay-kandimalla/
________________________________________
⭐ License
This project is open for academic use and portfolio demonstration.

