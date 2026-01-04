import os
import fitz  
from pathlib import Path

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"[ERROR] Could not read {pdf_path}: {e}")
    return text.strip()

def extract_text_from_txt(txt_path: str) -> str:
    """
    Extract text from a TXT file.
    """
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        print(f"[ERROR] Could not read {txt_path}: {e}")
        return ""

def parse_resume(file_path: str) -> str:
    """
    Parse a single resume file (PDF or TXT).
    """
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    else:
        print(f"[WARNING] Unsupported file format: {file_path}")
        return ""

def parse_all_resumes(resume_folder: str = "data/resumes") -> dict:
    """
    Parse all resumes in the given folder.
    Returns a dictionary {filename: extracted_text}.
    """
    parsed_resumes = {}
    if not os.path.exists(resume_folder):
        print(f"[ERROR] Resume folder not found: {resume_folder}")
        return parsed_resumes

    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)
        if os.path.isfile(file_path):
            parsed_resumes[filename] = parse_resume(file_path)
    return parsed_resumes

if __name__ == "__main__":
    resumes = parse_all_resumes()
    for name, text in resumes.items():
        print(f"\n--- {name} ---")
        print(text[:500])  # Print first 500 chars for preview
        print("...")
