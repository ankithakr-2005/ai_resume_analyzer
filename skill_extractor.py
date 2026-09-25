import re
from typing import Set

SKILL_TAXONOMY = {
    "Programming": ["python", "c++", "c#", "java", "javascript", "sql", "r", ".net"],
    "Data & Analytics": ["pandas", "numpy", "excel", "power bi", "tableau", "sql"],
    "Machine Learning & AI": ["scikit-learn", "ml", "deep learning", "llm", "rag", "nlp", "transformers", "hugging face", "opencv", "cnn", "yolo", "pytorch"],
    "DevOps & Tools": ["fastapi", "docker", "git", "aws", "mlflow", "apis"]
}

def get_all_skills() -> Set[str]:
    skills = set()
    for cat_skills in SKILL_TAXONOMY.values():
        skills.update(cat_skills)
    return skills

def extract_skills_from_text(cleaned_text: str) -> Set[str]:
    """Finds matching skills using word boundaries."""
    found_skills = set()
    all_skills = get_all_skills()
    
    for skill in all_skills:
        pattern = rf'\b{re.escape(skill)}\b'
        if re.search(pattern, cleaned_text):
            found_skills.add(skill)
            
    return found_skills