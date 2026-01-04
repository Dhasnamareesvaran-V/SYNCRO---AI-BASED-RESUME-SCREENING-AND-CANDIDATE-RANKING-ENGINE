SYNCRO - AI BASED RESUME SCREENING APP

OVERVIEW

Syncro is an AI‑powered resume screening application built during an internship at Bigsibucks Innovation Pvt Ltd. It automates resume parsing, job description (JD) matching, candidate ranking, and transparent scoring so recruiters can quickly identify top candidates with clear, explainable results. The project emphasizes modular design, reproducible setup, and a polished Streamlit UI tailored for real‑world recruiter workflows.

PROBLEM STATEMENT

Recruiters often spend significant time manually screening resumes to identify candidates who match job descriptions. This process is repetitive, error‑prone, and lacks transparency. There is a need for an automated system that can parse resumes, compare them against job descriptions, and provide clear, explainable scores and rankings to streamline hiring.

OBJECTIVES OF THE PROJECT

Automate resume parsing and text extraction from PDF/TXT files.
Implement keyword and semantic similarity matching between resumes and job descriptions.
Provide transparent scoring with percentages and star ratings for recruiter clarity.
Rank candidates based on match strength to highlight top talent quickly.
Deliver a polished, recruiter‑friendly UI with branding and professional presentation.

KEY FEATURES

Automated parsing: Extracts structured text from resumes (PDF/TXT) for downstream analysis.
JD matching: Compares resumes against recruiter‑provided JDs using keyword and semantic similarity.
Transparent scoring: Displays percentage scores and star ratings with simple, explainable logic.
Candidate ranking: Orders applicants by match strength to surface the most relevant profiles.
Polished UI/UX: Clean Streamlit interface with branding and recruiter‑friendly layout for clarity.

TECH STACK

Language: Python
Frontend: Streamlit

Core libraries:

sentence-transformers: Semantic similarity for JD–resume matching.
PyPDF2: PDF text extraction for resume parsing.
Pillow: Image handling for logos and UI assets.
Standard libs: os, re, collections for utilities and file operations.
Environment: Virtual environment (venv) with pinned dependencies in requirements.txt
Version control: Git + GitHub for code, docs, and issue tracking

PACKAGES

1.streamlit
2.pymupdf
3.pdfminer.six
4.spacy
5.sentence-transformers
6.scikit-learn
7.pandas
8.numpy

ARCHITECTURE AND WORKFLOW

Design principles: Modular architecture, clear separation of concerns (UI, logic, utilities, data), and reproducibility.

Conceptual flow:

User uploads: Resume(s) and JD(s) via Streamlit.
Parser module: Converts resume files into clean text.
Matcher module: Computes keyword overlap and semantic similarity to JD(s).
Ranker module: Sorts candidates by aggregated similarity metrics.
Scorer module: Produces percentage scores and star ratings.
UI output: Displays ranked results with explanations and branding.

[User Uploads Resume/JD]
↓
[Parser Module]
↓
[Matcher Module]
↓
[Ranker Module]
↓
[Scorer Module]
↓
[Streamlit UI Output]

PROJECT STRUCTURE

RESUME_SCREENING_PROJECT/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── .gitignore # VCS hygiene
│
├── modules/ # Core backend logic
│ ├── parser.py # Resume text extraction
│ ├── matcher.py # JD–resume similarity
│ ├── ranker.py # Candidate ordering
│ └── scorer.py # Transparent scoring
│
├── ui/ # UI components
│ └── upload_ui.py # Upload + layout helpers
│
├── utils/ # Utility helpers
│ └── file_handler.py # File ops + temp storage
│
├── data/ # Inputs & assets
│ ├── resumes/ # Candidate resumes
│ ├── job_descriptions/ # Recruiter JDs
│ ├── assets/ # Branding/logo
│ │ └── syncro_logo.png
│ └── temp_resume.pdf # Example/placeholder

INSTALLATION

Prerequisites: Python 3.10+, Git, and a working internet connection.

Create and activate a virtual environment:

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt

USAGE

Prepare inputs:
Resumes: Place PDF/TXT resumes in data/resumes/.
Job descriptions: Place JD files in data/job_descriptions/.

Run the app:
streamlit run app.py

Workflow in the UI:

Upload files: Select resume(s) and JD(s).
Process: App parses resumes, matches to JD, ranks and scores candidates.
Review results: See percentage scores, star ratings, and ranked list with explanations.
Upload interface: Demonstrates branding and clear inputs.
Parsing output: Shows extracted text for transparency.
Results page: Displays rankings and scores.

CONFIGURATION AND CUSTOMIZATION

Scoring weights: Adjust keyword vs. semantic contribution in modules/scorer.py.
Model selection: Swap or fine‑tune sentence-transformers model in modules/matcher.py.
Parsing rules: Customize text cleaning and extraction in modules/parser.py.
UI branding: Update logo and color scheme in data/assets/ and ui/upload_ui.py.
File constraints: Enforce allowed file types and size limits in utils/file_handler.py.

MODULES OVERVIEW

parser.py: Extracts and cleans text from resumes, handles edge cases (non‑selectable PDFs, mixed content).
matcher.py: Computes keyword overlap and semantic similarity using embeddings; outputs match vectors.
ranker.py: Aggregates similarity metrics and sorts candidates; supports tie‑breakers and thresholds.
scorer.py: Converts aggregated metrics into user‑friendly percentage scores and star ratings.
upload_ui.py: Provides streamlined upload controls, previews, and basic validation.
file_handler.py: Manages file I/O, temporary storage, and safe cleanup.

SAMPLE DATA

The project includes example resumes and job descriptions for quick testing:

Resumes: Stored in data/resumes/ (e.g., dataanalyst_resume.pdf, mlengineer_resume.pdf, webdeveloper_resume.pdf).
Job Descriptions: Stored in data/job_descriptions/ (e.g., dataanalyst_jd.txt, mlengineer_jd.txt, webdeveloper_jd.txt).
Assets: Logo and branding files in data/assets/.
Temp Files: Example resume (temp_resume.pdf) for demo purposes.

FUTURE ENHANCEMENTS

Multi‑JD Comparison: Evaluate a candidate against multiple roles simultaneously.
Section‑wise Scoring: Break down scores by skills, education, and experience for deeper insights.
Advanced NLP Models: Integrate contextual embeddings for richer semantic matching.
Explainability Features: Show recruiters why a candidate scored a certain way (highlight matched keywords/phrases).
Cloud Deployment: Host on Streamlit Cloud or Hugging Face Spaces for easy access and demo.
Integration with ATS: Connect with Applicant Tracking Systems to streamline recruiter workflows.
