# utils/scoring.py

def score_experience(resume_years, jd_text):
    """
    Compare resume experience with job description requirements.
    If JD mentions required years, compare them.
    If JD doesn't mention years, give full score.
    """
    import re

    # Look for "X years" requirement in job description
    match = re.search(r"(\d+)\+?\s*years?", jd_text.lower())
    
    if match:
        required = int(match.group(1))
        return min(1.0, resume_years / required)  # cap at 1.0
    else:
        return 1.0  # If JD doesn't mention years → full score


def score_education(resume_degree, jd_text):
    jd_text = jd_text.lower()

    # Prioritize: PhD > Master > Bachelor
    degree_rank = {
        "Not Found": 0,
        "Associate Degree": 1,
        "Bachelor's": 2,
        "Master's": 3,
        "PhD": 4
    }

    # Detect requirements
    required = 0
    if "phd" in jd_text or "doctorate" in jd_text:
        required = 4
    elif "master" in jd_text or "m.sc" in jd_text or "m.s" in jd_text or "mba" in jd_text:
        required = 3
    elif "bachelor" in jd_text or "b.sc" in jd_text or "b.s" in jd_text:
        required = 2

    resume_rank = degree_rank.get(resume_degree, 0)

    return 1.0 if resume_rank >= required else resume_rank / max(required, 1)


def final_ats_score(skill_match, bert_sim, tfidf_sim, exp_score, edu_score):
    """
    Weighted ATS Score (0–100)
    """
    final = (
        skill_match * 0.40 +
        bert_sim * 0.30 +
        tfidf_sim * 0.10 +
        exp_score * 0.10 +
        edu_score * 0.10
    )
    return round(final * 100, 2)