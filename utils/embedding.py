# utils/embedding.py

from sentence_transformers import SentenceTransformer, util
import os

# ---------------------------------------------------------
# Load LOCAL SBERT model (required for Streamlit Cloud)
# ---------------------------------------------------------

# Path to this file: utils/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root folder: capstone_project/
ROOT_DIR = os.path.dirname(BASE_DIR)

# Local model path inside: capstone_project/models/all-MiniLM-L6-v2/
MODEL_PATH = os.path.join(ROOT_DIR, "models", "all-MiniLM-L6-v2")

# Load SBERT model from local folder
bert_model = SentenceTransformer(MODEL_PATH)


def get_embedding(text: str):
    """Convert text into BERT embedding tensor."""
    return bert_model.encode(text, convert_to_tensor=True)


def compute_bert_similarity(text1: str, text2: str):
    """Compute semantic similarity between two texts using BERT."""
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    score = util.cos_sim(emb1, emb2)[0][0]
    return float(score)