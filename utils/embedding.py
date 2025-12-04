# utils/embedding.py

import os
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# ------------------------------------------
# Load LOCAL SBERT MODEL from /models/
# ------------------------------------------

# Path: utils/ → go to project root
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

# Full local SBERT model path
MODEL_PATH = os.path.join(ROOT_DIR, "models", "all-MiniLM-L6-v2")

# Load from local folder (NO HF DOWNLOAD)
bert_model = SentenceTransformer(MODEL_PATH, device="cpu")


def get_embedding(text):
    """Return SBERT embedding vector."""
    return bert_model.encode(text, convert_to_tensor=True)


def compute_bert_similarity(text1, text2):
    """Compute semantic similarity between texts."""
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    score = cos_sim(emb1, emb2)[0][0]
    return float(score)