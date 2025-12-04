import os
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.text_cleaner import clean_text

# Determine model path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Load models
tfidf = joblib.load(os.path.join(MODELS_DIR, "tfidf_vectorizer.pkl"))
hybrid_model = joblib.load(os.path.join(MODELS_DIR, "resume_hybrid_model.pkl"))

# Load BERT model name
with open(os.path.join(MODELS_DIR, "bert_model_name.txt"), "r") as f:
    bert_model_name = f.read().strip()

bert = SentenceTransformer(bert_model_name)

def predict_category(resume_text: str) -> str:
    """
    Runs hybrid prediction:
    BERT + TF-IDF → LinearSVC
    """
    # Cleaned text for TF-IDF
    cleaned = clean_text(resume_text)

    # TF-IDF vector
    vec_tfidf = tfidf.transform([cleaned]).toarray()

    # BERT vector (use raw text)
    vec_bert = bert.encode([resume_text])

    # Hybrid feature = [BERT | TF-IDF]
    hybrid_vec = np.hstack([vec_bert, vec_tfidf])

    # Predict category
    pred = hybrid_model.predict(hybrid_vec)[0]
    return pred