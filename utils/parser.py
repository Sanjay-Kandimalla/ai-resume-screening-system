# utils/parser.py

import fitz  # PyMuPDF
import docx2txt
import re
import tempfile
import os

def extract_text_from_pdf_bytes(file_bytes: bytes) -> str:
    """Extract text from a PDF file given as bytes."""
    text = ""
    with fitz.open(stream=file_bytes, filetype="pdf") as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def extract_text_from_docx_bytes(file_bytes: bytes) -> str:
    """Extract text from a DOCX file given as bytes."""
    # docx2txt needs a file path, so we write to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    try:
        text = docx2txt.process(tmp_path)
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return text

def extract_text_from_upload(uploaded_file):
    """
    Streamlit uploaded_file -> clean text string.
    Supports .pdf and .docx.
    """
    if uploaded_file is None:
        return ""

    file_bytes = uploaded_file.read()
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        return extract_text_from_pdf_bytes(file_bytes)
    elif name.endswith(".docx"):
        return extract_text_from_docx_bytes(file_bytes)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX resume.")

def extract_contact_details(text: str):
    """
    Extract simple contact details (email, phone) from raw resume text.
    """
    email_matches = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    phone_matches = re.findall(r"\+?\d[\d \-()]{8,}\d", text)

    email = email_matches[0] if email_matches else None
    phone = phone_matches[0] if phone_matches else None

    return {
        "email": email,
        "phone": phone
    }
import re

def extract_experience_years(text: str):
    """
    Extract years of experience based on common resume patterns.
    Examples detected:
    - "3 years of experience"
    - "5+ years"
    - "2 yrs"
    """
    patterns = [
        r"(\d+)\+?\s*years?",
        r"(\d+)\s*yrs?",
    ]
    years = []

    for p in patterns:
        matches = re.findall(p, text.lower())
        for m in matches:
            try:
                years.append(int(m))
            except:
                pass

    return max(years) if years else 0


def extract_education_level(text: str):
    """
    Detect highest education degree mentioned in resume.
    """
    text = text.lower()

    if "phd" in text or "doctorate" in text:
        return "PhD"
    if "master" in text or "m.sc" in text or "m.s" in text or "mba" in text or "m.tech" in text:
        return "Master's"
    if "bachelor" in text or "b.sc" in text or "b.s" in text or "b.tech" in text:
        return "Bachelor's"
    if "associate" in text:
        return "Associate Degree"

    return "Not Found"