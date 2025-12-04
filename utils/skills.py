# utils/skills.py

# Basic skill dictionary (you can expand this later)
SKILL_SET = {
    # Programming
    "python", "java", "c++", "c#", "javascript", "typescript",
    "r", "sql", "nosql", "scala",

    # Data / ML
    "machine learning", "deep learning", "nlp", "computer vision",
    "predictive analytics", "data mining",

    # Libraries / Tools
    "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn",
    "tensorflow", "pytorch",

    # BI Tools
    "power bi", "tableau", "looker studio",

    # Cloud
    "aws", "azure", "gcp", "snowflake", "databricks",

    # Databases
    "mysql", "postgresql", "mongodb", "oracle",

    # Soft skills
    "problem solving", "communication", "leadership",
}

def extract_skills(text: str):
    """
    Extract skills from text using simple keyword matching.
    """
    text_lower = text.lower()
    found = []

    for skill in SKILL_SET:
        if skill in text_lower:
            found.append(skill)

    return sorted(list(set(found)))