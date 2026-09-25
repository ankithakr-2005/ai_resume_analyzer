from typing import List, Dict

# Comprehensive mapping of technical skills to specific learning modules
ROADMAP_TEMPLATES: Dict[str, str] = {
    # Data Analytics & Visualization
    "excel": "Practice Advanced Formulas (VLOOKUP, INDEX/MATCH, XLOOKUP) and Pivot Tables.",
    "pandas": "Learn Data Wrangling, Manipulations, and Aggregations using Pandas DataFrames.",
    "power bi": "Learn DAX formulas, Data Modeling, and build interactive analytical dashboards.",
    "tableau": "Build interactive visualizations, calculated fields, and executive dashboards.",
    "sql": "Master complex JOINs, Window Functions, Aggregations, and Subqueries.",
    
    # Machine Learning & Data Science
    "scikit-learn": "Practice supervised ML pipelines, cross-validation, and hyperparameter tuning.",
    "ml": "Understand core algorithms (Regression, Decision Trees, Ensembles) and evaluation metrics.",
    "deep learning": "Study Neural Network architectures, backpropagation, and activation functions.",
    "opencv": "Implement Image Processing techniques, edge detection, and feature extraction.",
    "cnn": "Build Convolutional Neural Networks for image classification and feature mapping.",
    "yolo": "Implement real-time object detection models using modern YOLO versions.",
    "pytorch": "Construct custom neural networks, loss functions, and training loops in PyTorch.",
    
    # NLP & GenAI
    "nlp": "Master text preprocessing, tokenization, TF-IDF, and word embeddings (Word2Vec, GloVe).",
    "transformers": "Fine-tune pre-trained Hugging Face transformer models for NLP downstream tasks.",
    "spacy": "Perform Named Entity Recognition (NER), POS tagging, and custom pipeline construction.",
    "llm": "Understand Large Language Model architecture, prompt engineering, and fine-tuning techniques.",
    "rag": "Implement Retrieval-Augmented Generation using LangChain, LlamaIndex, and Vector DBs.",
    
    # DevOps, APIs & MLOps
    "fastapi": "Build scalable RESTful APIs with FastAPI and Pydantic data validation.",
    "docker": "Containerize Python applications with Dockerfiles and multi-container Docker Compose.",
    "apis": "Design and consume RESTful APIs, handling authentication and JSON payloads.",
    "aws": "Learn Cloud deployment fundamentals using AWS S3, EC2, and Lambda.",
    "mlflow": "Track experiment metrics, log model artifacts, and manage the ML model lifecycle.",
    "git": "Master Version Control, branching strategies, pull requests, and Git workflows."
}

def generate_roadmap(missing_skills: List[str]) -> List[str]:
    """
    Generates a structured, week-by-week learning roadmap 
    based on identified missing skills for a target job role.
    """
    if not missing_skills:
        return ["You already possess all key skills listed for this target role! Focus on building advanced projects."]

    roadmap: List[str] = []
    
    for idx, skill in enumerate(missing_skills, start=1):
        skill_clean = skill.strip().lower()
        
        # Check if the missing skill exists in our template dictionary
        if skill_clean in ROADMAP_TEMPLATES:
            detail = ROADMAP_TEMPLATES[skill_clean]
            roadmap.append(f"**Week {idx} ({skill.title()}):** {detail}")
        else:
            # Fallback for skills not in the predefined template dictionary
            roadmap.append(f"**Week {idx} ({skill.title()}):** Focus on fundamental concepts, hands-on tutorials, and practical projects in **{skill.title()}**.")
            
    return roadmap