import streamlit as st
from typing import Dict, Any, List, Union


def render_resume_page(
    candidate_name: str,
    score: Union[Dict[str, Any], float, int],
    score_label: str,
    skills: List[str],
    sections: Dict[str, str],
) -> None:
    """
    Renders the detailed Resume Analysis and ATS feedback page.
    """
    st.title("📄 Detailed Resume Analysis")
    st.write(f"Candidate: **{candidate_name}**")

    # Extract numerical overall score safely whether score is dict or float
    if isinstance(score, dict):
        overall_score = score.get("overall_score", 0.0)
        score_data = score
    else:
        overall_score = float(score) if score else 0.0
        score_data = {}

    # Score Overview Header
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <h4>Overall ATS Score</h4>
                <div class="metric-value">{overall_score:.1f}/100</div>
                <p style="margin-top: 8px; font-weight: 600; color: #2563eb;">{score_label}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        if score_data:
            st.subheader("ATS Performance Breakdown")
            b_col1, b_col2, b_col3, b_col4 = st.columns(4)
            with b_col1:
                st.metric("ATS Match", f"{score_data.get('ats_compatibility', 0)}%")
            with b_col2:
                st.metric("Content", f"{score_data.get('content_quality', 0)}%")
            with b_col3:
                st.metric("Skills", f"{score_data.get('skill_strength', 0)}%")
            with b_col4:
                st.metric("Impact", f"{score_data.get('impact_strength', 0)}%")

    st.markdown("---")

    # Detailed Feedback Section
    if score_data:
        st.subheader("🔍 ATS & Quality Diagnostic")

        f_col1, f_col2 = st.columns(2)

        with f_col1:
            st.markdown("### ✅ What is Working Well")
            goods = score_data.get("what_is_good", [])
            if goods:
                for item in goods:
                    st.markdown(f"- <span class='feedback-good'>{item}</span>", unsafe_allow_html=True)
            else:
                st.write("No strong highlights detected yet.")

            st.markdown("### ⚠️ Areas Needing Improvement")
            warns = score_data.get("needs_improvement", [])
            if warns:
                for item in warns:
                    st.markdown(f"- <span class='feedback-warn'>{item}</span>", unsafe_allow_html=True)
            else:
                st.write("No major weaknesses detected.")

        with f_col2:
            st.markdown("### 🛠️ Actionable Specific Fixes")
            fixes = score_data.get("actionable_fixes", [])
            if fixes:
                for idx, fix in enumerate(fixes, 1):
                    st.markdown(f"**{idx}.** {fix}")
            else:
                st.write("Your resume structure aligns well with standard requirements.")

        st.markdown("---")

    # Skills Section
    st.subheader(f"🛠️ Extracted Skills ({len(skills)})")
    if skills:
        badges_html = " ".join([f'<span class="skill-badge">{s}</span>' for s in skills])
        st.markdown(badges_html, unsafe_allow_html=True)
    else:
        st.info("No skills detected. Consider adding a clear 'Skills' section header.")

    st.markdown("---")

    # Parsed Sections Inspector
    st.subheader("📑 Detected Resume Sections")
    if sections:
        tabs = st.tabs([sec.title() for sec in sections.keys()])
        for tab, (sec_name, sec_content) in zip(tabs, sections.items()):
            with tab:
                st.text_area(
                    label=f"Content for {sec_name.title()}",
                    value=sec_content,
                    height=200,
                    disabled=True,
                )
    else:
        st.warning("No structured sections detected in the uploaded PDF.")