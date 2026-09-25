# AI Resume Analyzer & Job Recommendation System

An NLP-powered application that parses candidate resumes (PDF/DOCX), extracts technical skills, calculates job match scores using TF-IDF and Cosine Similarity, and generates a personalized learning roadmap.

## Key Features
- **Resume Text Extraction**: Extracts text from PDF and DOCX files using `pypdf` and `python-docx`.
- **Text Preprocessing**: Normalizes text while preserving technical symbols like C++, C#, and .NET.
- **Skill Extraction**: Matches candidate technical skills against a defined taxonomy using boundary-aware regex.
- **Job Matching**: Evaluates vector alignment between resume text and job descriptions using TF-IDF and Cosine Similarity.
- **Skill Gap & Roadmap**: Highlights matching vs. missing skills for selected job roles and builds a weekly learning roadmap.

## Setup & Execution

1. **Activate Virtual Environment:**
   ```powershell
   .\venv\Scripts\Activate.ps1

1. Install Dependencies:
python -m pip install -r requirements.txt

2. Run Streamlit Application:
python -m streamlit run app.py

