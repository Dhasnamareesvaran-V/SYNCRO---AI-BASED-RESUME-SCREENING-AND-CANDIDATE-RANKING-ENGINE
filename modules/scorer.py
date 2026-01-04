import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.parser import parse_all_resumes
from modules.matcher import match_all, load_job_description

def normalize_score(similarity: float) -> int:
    """
    Convert cosine similarity (0–1) into a 0–100 score.
    """
    return int(similarity * 100)

def extract_keywords(text: str) -> list:
    """
    Very simple keyword extractor (split by non-alphabetic chars).
    """
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return list(set(words))

def score_resume_against_jd(resume_text: str, jd_text: str, similarity: float) -> dict:
    """
    Generate a transparent score report for a resume vs JD.
    """
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched_keywords = [kw for kw in jd_keywords if kw in resume_keywords]
    keyword_match_ratio = len(matched_keywords) / len(jd_keywords) if jd_keywords else 0

    return {
        "similarity_score": normalize_score(similarity),
        "keyword_match_ratio": round(keyword_match_ratio * 100, 2),
        "matched_keywords": matched_keywords
    }

if __name__ == "__main__":
    resumes = parse_all_resumes()
    matches = match_all(resumes)

    for resume, jd_scores in matches.items():
        print(f"\n--- {resume} ---")
        for jd, sim in jd_scores.items():
            jd_text = load_job_description(f"data/job_descriptions/{jd}")
            report = score_resume_against_jd(resumes[resume], jd_text, sim)
            print(f"{jd}: {report}")
