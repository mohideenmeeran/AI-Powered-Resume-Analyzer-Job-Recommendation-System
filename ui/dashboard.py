import streamlit as st
from typing import Dict, Any, List


def render_dashboard(
    candidate_name: str,
    score_data: Dict[str, Any],
    skill_count: int,
    job_results: List[Dict[str, Any]],
    recommendations: Dict[str, Any],
) -> None:
    """
    Renders executive candidate overview dashboard with modern UI components.
    """
    # SaaS Hero Header Banner
    st.markdown(
        f"""
        <div class="hero-header">
            <h1>Candidate Dashboard: {candidate_name}</h1>
            <p>Real-time analytics on ATS compatibility, target role suitability, and high-impact career recommendations.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    score_val = (
        score_data.get("overall_score", 0.0)
        if isinstance(score_data, dict)
        else float(score_data)
    )
    top_role = (
        job_results[0]["title"]
        if job_results
        else "Data Science / Developer Candidate"
    )
    top_fit = job_results[0]["match_score"] if job_results else 0.0

    # Key Metrics Scorecards
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <h4>Resume Health Score</h4>
                <div class="metric-value">{score_val:.1f} <span style="font-size:14px; color:#64748b;">/ 100</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <h4>Top Career Match</h4>
                <div class="metric-value" style="color:#166534;">{top_fit}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <h4>Detected Skills</h4>
                <div class="metric-value">{skill_count}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="metric-card">
                <h4>Primary Target Role</h4>
                <div class="metric-value" style="font-size:18px; color:#1e293b; margin-top:4px;">{top_role}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Immediate High-Impact Actions
    st.subheader("💡 Your High-Impact Next Actions")

    fixes = (
        score_data.get("actionable_fixes", [])
        if isinstance(score_data, dict)
        else []
    )

    default_actions = [
        "Incorporate measurable outcomes (e.g., percentages, dataset size) in project descriptions.",
        f"Build one targeted project focusing on core requirements for {top_role}.",
        "Include missing standard headings to improve ATS extraction score.",
    ]

    actions_to_show = fixes[:3] if fixes else default_actions

    for idx, act in enumerate(actions_to_show, 1):
        st.info(f"**Action {idx}:** {act}")