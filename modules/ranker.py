import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.parser import parse_all_resumes
from modules.matcher import match_all, load_job_description
from modules.scorer import score_resume_against_jd

def rank_resumes(resumes: dict, jd_folder: str = "data/job_descriptions") -> dict:
    """
    Rank resumes against job descriptions and return best match with score.
    """
    matches = match_all(resumes)
    results = {}

    for resume_name, jd_scores in matches.items():
        best_jd = max(jd_scores, key=jd_scores.get)
        best_score = jd_scores[best_jd]

        jd_text = load_job_description(os.path.join(jd_folder, best_jd))
        report = score_resume_against_jd(resumes[resume_name], jd_text, best_score)

        results[resume_name] = {
            "best_match": best_jd.replace("_jd.txt", "").title(),
            "score": report["similarity_score"],
            "keyword_match_ratio": report["keyword_match_ratio"],
            "matched_keywords": report["matched_keywords"]
        }
    return results

if __name__ == "__main__":
    resumes = parse_all_resumes()
    ranked = rank_resumes(resumes)

    for resume, result in ranked.items():
        print(f"\nResume: {resume}")
        print(f"Best Match: {result['best_match']}")
        print(f"Score: {result['score']}/100")
        print(f"Keyword Match Ratio: {result['keyword_match_ratio']}%")
        print(f"Matched Keywords: {', '.join(result['matched_keywords'])}")
