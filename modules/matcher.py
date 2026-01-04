import os
import sys
from sentence_transformers import SentenceTransformer, util

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.parser import parse_all_resumes


def load_job_description(jd_path: str) -> str:
    """
    Load job description text from a file.
    """
    try:
        with open(jd_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        print(f"[ERROR] Could not read {jd_path}: {e}")
        return ""


def compute_similarity(resume_text: str, jd_text: str, model=None) -> float:
    """
    Compute cosine similarity between resume and job description embeddings.
    """
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')

    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    jd_emb = model.encode(jd_text, convert_to_tensor=True)

    similarity = util.cos_sim(resume_emb, jd_emb)
    return float(similarity)


def match_all(resumes: dict, jd_folder: str = "data/job_descriptions") -> dict:
    """
    Match all resumes against all job descriptions.
    Returns {resume_name: {jd_name: similarity_score}}.
    """
    model = SentenceTransformer('all-MiniLM-L6-v2')
    results = {}

    if not os.path.exists(jd_folder):
        print(f"[ERROR] Job description folder not found: {jd_folder}")
        return results

    for resume_name, resume_text in resumes.items():
        results[resume_name] = {}
        for jd_file in os.listdir(jd_folder):
            jd_path = os.path.join(jd_folder, jd_file)
            if os.path.isfile(jd_path):
                jd_text = load_job_description(jd_path)
                score = compute_similarity(resume_text, jd_text, model)
                results[resume_name][jd_file] = round(score, 4)
    return results

if __name__ == "__main__":
    resumes = parse_all_resumes()
    matches = match_all(resumes)

    for resume, jd_scores in matches.items():
        print(f"\n--- {resume} ---")
        for jd, score in jd_scores.items():
            print(f"{jd}: {score}")
