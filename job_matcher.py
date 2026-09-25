import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Set, Tuple, List

def calculate_role_matches(cleaned_resume_text: str, job_roles_df: pd.DataFrame) -> pd.DataFrame:
    """Calculates match percentage against all job descriptions."""
    corpus = [cleaned_resume_text] + job_roles_df['description'].tolist()
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Calculate similarity of index 0 (resume) against indices 1..N (jobs)
    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    results_df = job_roles_df.copy()
    results_df['match_score'] = (scores * 100).round(1)
    return results_df.sort_values(by='match_score', ascending=False)

def analyze_skill_gap(candidate_skills: Set[str], required_skills_str: str) -> Tuple[List[str], List[str]]:
    """Identifies candidate's matching and missing skills for a target role."""
    required = [s.strip().lower() for s in required_skills_str.split(",")]
    found = [s for s in required if s in candidate_skills]
    missing = [s for s in required if s not in candidate_skills]
    return found, missing