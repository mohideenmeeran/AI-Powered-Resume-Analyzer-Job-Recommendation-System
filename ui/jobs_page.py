import streamlit as st
import plotly.graph_objects as go
from typing import List, Dict, Any


def render_jobs_page(job_results: List[Dict[str, Any]]) -> None:
    """
    Renders Target Career Fit page with an interactive Plotly Radar comparison chart.
    """
    st.title("🎯 Role Fit Comparison & Job Recommendations")
    st.write(
        "Evaluate your profile compatibility across technical roles and identify skill gaps."
    )

    if not job_results:
        st.warning("No role recommendations available. Please upload a resume first.")
        return

    st.markdown("---")

    # Plotly Radar Chart Comparison
    st.subheader("📊 Career Compatibility Radar")

    roles = [r.get("title", "Role") for r in job_results]
    scores = [r.get("match_score", 0.0) for r in job_results]

    # Close radar loop
    radar_roles = roles + [roles[0]]
    radar_scores = scores + [scores[0]]

    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=radar_scores,
            theta=radar_roles,
            fill="toself",
            name="Match Score",
            line_color="#2563eb",
            fillcolor="rgba(37, 99, 235, 0.2)",
        )
    )

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        height=380,
        margin=dict(l=40, r=40, t=20, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Itemized Target Roles List
    st.subheader("💼 Recommended Roles Breakdown")

    for idx, result in enumerate(job_results, 1):
        role_title = result.get("title", "Target Role")
        match_score = result.get("match_score", 0.0)
        matched_skills = result.get("matched_skills", [])
        missing_req = result.get("missing_required", [])
        missing_rec = result.get("missing_recommended", [])
        next_step = result.get(
            "recommended_next_step",
            "Focus on practical project implementations.",
        )

        with st.expander(
            f"**{idx}. {role_title}** — {match_score}% Match Score",
            expanded=(idx == 1),
        ):
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**✓ Matching Skills Possessed:**")
                if matched_skills:
                    badges = " ".join(
                        [
                            f'<span class="skill-badge skill-badge-matched">{s}</span>'
                            for s in matched_skills
                        ]
                    )
                    st.markdown(badges, unsafe_allow_html=True)
                else:
                    st.write("No direct matches.")

            with col2:
                st.markdown("**⚠ Required Skills to Acquire:**")
                all_missing = missing_req + missing_rec
                if all_missing:
                    missing_badges = " ".join(
                        [
                            f'<span class="skill-badge skill-badge-missing">{s}</span>'
                            for s in all_missing
                        ]
                    )
                    st.markdown(missing_badges, unsafe_allow_html=True)
                else:
                    st.success("You meet all core skill requirements!")

            st.info(f"💡 **Recommended Action Step:** {next_step}")