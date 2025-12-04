import streamlit as st
from bootstrap import *

# Page Config
st.set_page_config(page_title="Contact", page_icon="📬", layout="wide")


# ------------------------------------------
# CONTACT PAGE CONTENT
# ------------------------------------------

st.markdown("""
# 📬 Contact & Credits  
### Developed by **Sanjay Kandimalla**

**Master of Science – Applied Statistics & Data Science**  
University of Texas at Arlington  
📍 Arlington, Texas  
""")

st.markdown("---")

# -----------------------------
# Contact Info with Icons
# -----------------------------
st.markdown("""
## 📧 Contact Information  

📩 **Email:**  
**sanjay.kandimalla2025@gmail.com**

📱 **Phone:**  
**+1 (682) 888-7580**

🔗 **LinkedIn:**  
[linkedin.com/in/sanjay-kandimalla](https://www.linkedin.com/in/sanjay-kandimalla)
""")

st.markdown("---")

# -----------------------------
# Technologies Used
# -----------------------------
st.markdown("""
## 🛠 Technologies Used  

| Category         | Tools |
|------------------|-------|
| **NLP**          | Regex, Custom Parsing, BERT Embeddings |
| **ML Models**    | TF-IDF + SVM, Hybrid Classifier |
| **Visualization**| Plotly, Streamlit |
| **Deployment**   | Streamlit Multipage App |
| **PDF Reports**  | FPDF2 |
| **Programming**  | Python |
""")

st.markdown("---")

# -----------------------------
# Capstone Description
# -----------------------------
st.markdown("""
## ⭐ Capstone Project Overview  

This system demonstrates:

- End-to-end AI/NLP system design  
- Practical ML deployment workflow  
- Resume–JD matching  
- Skills extraction & semantic scoring  
- ATS-style analytics  
- Premium PDF reporting  

It simulates a **professional-grade ATS platform** using  
**Machine Learning + NLP + Semantic Embeddings**.

---

If you're viewing this tool, feel free to reach out for:

- 🤝 Collaboration  
- 📚 Research discussions  
- 🧠 Professional networking  
- 📝 Resume analysis guidance  
""")

st.success("Thank you for visiting! Looking forward to connecting.")