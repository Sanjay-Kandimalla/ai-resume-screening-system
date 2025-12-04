# utils/embedding.py

from sentence_transformers import SentenceTransformer, util

# Load BERT model once
bert_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str):
    """Convert text into BERT embedding tensor."""
    return bert_model.encode(text, convert_to_tensor=True)

def compute_bert_similarity(text1: str, text2: str):
    """Compute semantic similarity between two texts using BERT."""
    emb1 = get_embedding(text1)
    emb2 = get_embedding(text2)
    score = util.cos_sim(emb1, emb2)[0][0]
    return float(score)