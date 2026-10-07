import pandas as pd
import streamlit as st
from config import UPLOAD_DIR
from database.database import (
    get_analysis_history,
    initialize_database,
    save_analysis,
)
from services.jobs.job_search import rank_jobs
from services.recommendation.recommender import generate_recommendations
from services.resume.pdf_parser import extract_text_from_pdf
from services.resume.resume_scorer import (
    calculate_resume_score,
    get_score_label,
)
from services.resume.section_parser import (
    extract_candidate_name,
    parse_sections,
)
from services.resume.skill_extractor import extract_skills
from ui.dashboard import render_dashboard
from ui.jobs_page import render_jobs_page
from ui.mock_interview_page import render_mock_interview_page
from ui.resume_page import render_resume_page
from ui.skill_gap_page import render_skill_gap_page
from ui.styles import load_css

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------

st.set_page_config(
    page_title="Career Intelligence Platform",
    page_icon="💼",
    layout="wide",
)

st.markdown(
    load_css(),
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Database Setup
# ---------------------------------------------------------

initialize_database()


# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "job_results" not in st.session_state:
    st.session_state.job_results = []

if "recommendations" not in st.session_state:
    st.session_state.recommendations = {
        "skill_gaps": [],
        "learning_plan": [],
    }


# ---------------------------------------------------------
# Sidebar Navigation & Upload
# ---------------------------------------------------------

st.sidebar.title("Career Intelligence")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Resume Analysis",
        "Career Fit & Jobs",
        "Skill Gap & Roadmap",
        "AI HR Voice Interview",
        "History",
    ],
)

if page in [
    "Dashboard",
    "Resume Analysis",
    "Career Fit & Jobs",
    "Skill Gap & Roadmap",
    "AI HR Voice Interview",
]:
    uploaded_file = st.sidebar.file_uploader(
        "Upload PDF Resume",
        type=["pdf"],
    )

    if uploaded_file is not None:
        file_bytes = uploaded_file.getvalue()

        # Step 1: Extract Text
        text = extract_text_from_pdf(file_bytes)

        if not text:
            st.sidebar.error(
                "Unable to extract readable text from PDF. Please upload a non-scanned PDF."
            )
        else:
            # Step 2: Parse Sections, Candidate Name & Skills
            sections = parse_sections(text)
            candidate_name = extract_candidate_name(text)
            skills = extract_skills(text)

            # Step 3: Detailed ATS & Resume Evaluation
            score_data = calculate_resume_score(
                sections=sections,
                skills=skills,
                full_text=text,
            )
            score_label = get_score_label(score_data)

            # Step 4: Multi-Role Fit Ranking & Skill Gap
            job_results = rank_jobs(
                resume_text=text,
                resume_skills=skills,
                sections=sections,
                top_n=5,
            )

            # Step 5: Actionable Learning Roadmap
            recommendations = generate_recommendations(job_results)

            # Store results in Session State
            st.session_state.analysis = {
                "candidate_name": candidate_name,
                "full_text": text,
                "sections": sections,
                "skills": skills,
                "score_data": score_data,
                "score_label": score_label,
                "file_name": uploaded_file.name,
            }

            st.session_state.job_results = job_results
            st.session_state.recommendations = recommendations

            # Save uploaded PDF locally
            upload_path = UPLOAD_DIR / uploaded_file.name
            with open(upload_path, "wb") as file:
                file.write(file_bytes)

            # Persist record in SQLite DB
            save_analysis(
                file_name=uploaded_file.name,
                candidate_name=candidate_name,
                resume_score=score_data.get("overall_score", 0.0),
                skills=skills,
            )

            st.sidebar.success("Resume analyzed successfully!")


# ---------------------------------------------------------
# Current Analysis View Routing
# ---------------------------------------------------------

analysis = st.session_state.analysis


if page == "Dashboard":
    if analysis:
        render_dashboard(
            candidate_name=analysis["candidate_name"],
            score_data=analysis["score_data"],
            skill_count=len(analysis["skills"]),
            job_results=st.session_state.job_results,
            recommendations=st.session_state.recommendations,
        )
    else:
        st.title("Career Intelligence Platform")
        st.write("Upload your PDF resume from the sidebar to begin analysis.")
        st.info(
            "The system evaluates resume layout quality, calculates ATS metrics, "
            "ranks candidate suitability across tech roles, and generates a personalized learning plan."
        )


elif page == "Resume Analysis":
    if not analysis:
        st.warning("Please upload a resume first.")
    else:
        render_resume_page(
            candidate_name=analysis["candidate_name"],
            score=analysis["score_data"],
            score_label=analysis["score_label"],
            skills=analysis["skills"],
            sections=analysis["sections"],
        )


elif page == "Career Fit & Jobs":
    render_jobs_page(st.session_state.job_results)


elif page == "Skill Gap & Roadmap":
    render_skill_gap_page(st.session_state.recommendations)


elif page == "AI HR Voice Interview":
    if not analysis:
        st.warning("Please upload a resume first.")
    else:
        render_mock_interview_page(analysis["skills"])


elif page == "History":
    st.title("Analysis History")

    history = get_analysis_history()

    if not history:
        st.info("No previous analyses found in database.")
    else:
        dataframe = pd.DataFrame(
            history,
            columns=[
                "ID",
                "File Name",
                "Candidate Name",
                "Resume Score",
                "Skills Identified",
                "Timestamp",
            ],
        )

        st.dataframe(
            dataframe,
            use_container_width=True,
        )