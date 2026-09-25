import streamlit as st
import pandas as pd
from io import BytesIO
import plotly.express as px

from text_cleaner import extract_text_from_pdf, extract_text_from_docx, clean_text
from skill_extractor import extract_skills_from_text
from job_matcher import calculate_role_matches, analyze_skill_gap
from roadmap_generator import generate_roadmap

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer & Job Recommendation System")
st.write("Upload your resume to calculate role fit, detect skill gaps, and get a tailored learning roadmap.")

# Load dataset
@st.cache_data
def load_jobs():
    return pd.read_csv("data/job_roles.csv")

job_roles_df = load_jobs()

# File Uploader
uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    bytes_data = BytesIO(uploaded_file.getvalue())
    filename = uploaded_file.name.lower()
    
    # Text Extraction
    if filename.endswith(".pdf"):
        raw_text = extract_text_from_pdf(bytes_data)
    else:
        raw_text = extract_text_from_docx(bytes_data)
        
    cleaned_text = clean_text(raw_text)
    candidate_skills = extract_skills_from_text(cleaned_text)
    
    st.success("Resume processed successfully!")
    
    # Layout columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🛠 Extracted Technical Skills")
        if candidate_skills:
            st.write(", ".join([f"`{s.title()}`" for s in candidate_skills]))
        else:
            st.warning("No explicit technical skills detected from taxonomy dictionary.")

    # Match scores
    match_df = calculate_role_matches(cleaned_text, job_roles_df)
    
    with col2:
        st.subheader("🎯 Job Match Scores")
        fig = px.bar(match_df, x="match_score", y="role", orientation='h', 
                     title="Role Fit Percentage", labels={'match_score': 'Match Score (%)', 'role': 'Job Role'})
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Skill Gap & Target Role Analysis
    st.subheader("🔎 Target Role Skill Gap Analysis")
    selected_role = st.selectbox("Select Target Role for Detailed Feedback:", match_df["role"].tolist())
    
    role_data = match_df[match_df["role"] == selected_role].iloc[0]
    found_skills, missing_skills = analyze_skill_gap(candidate_skills, role_data["required_skills"])
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.success(f"**Skills Found for {selected_role}:**")
        st.write(", ".join(found_skills) if found_skills else "None")
        
    with g_col2:
        st.error(f"**Missing Skills for {selected_role}:**")
        st.write(", ".join(missing_skills) if missing_skills else "No skill gap detected!")

    st.divider()

    # Learning Roadmap Output
    if missing_skills:
        st.subheader("🚀 Personalized Learning Roadmap")
        roadmap_steps = generate_roadmap(missing_skills)
        for idx, step in enumerate(roadmap_steps, 1):
            st.markdown(f"**Step {idx}:** {step}")