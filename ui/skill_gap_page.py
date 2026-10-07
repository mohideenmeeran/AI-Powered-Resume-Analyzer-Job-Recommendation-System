import streamlit as st
from typing import Dict, Any, List


def render_skill_gap_page(recommendations: Dict[str, Any]) -> None:
    """
    Renders the Personalized Skill Gap Analysis and Multi-Week Learning Roadmap page.
    """
    st.title("🗺️ Skill Gap Analysis & Learning Roadmap")
    st.write(
        "Here is your personalized skill gap breakdown and step-by-step roadmap to make your profile "
        "100% competitive for your top target career path."
    )

    if not recommendations or not recommendations.get("skill_gaps"):
        st.warning("No skill gap analysis available. Please upload a resume first.")
        return

    target_role = recommendations.get("target_role", "Target Role")
    st.subheader(f"Target Career Path: {target_role}")

    st.markdown("---")

    # 1. Prioritized Skill Gaps
    st.subheader("🎯 Prioritized Skill Gaps")
    skill_gaps = recommendations.get("skill_gaps", [])

    col1, col2, col3 = st.columns(3)

    for idx, gap in enumerate(skill_gaps):
        priority_label = gap.get("priority", f"Priority {idx+1}")
        skills_list = gap.get("skills", [])

        target_col = [col1, col2, col3][idx % 3]

        with target_col:
            st.markdown(f"#### {priority_label}")
            if skills_list:
                for s in skills_list:
                    if isinstance(s, str):
                        if s in [
                            "Core role alignment is solid!",
                            "No immediate critical secondary gaps.",
                            "Advanced optimization skills.",
                        ]:
                            st.info(s)
                        else:
                            # Render clean native Streamlit badges
                            st.markdown(
                                f"• **{s.title()}**"
                            )
            else:
                st.write("None detected.")

    st.markdown("---")

    # 2. Multi-Week Actionable Learning Roadmap
    st.subheader("📅 Personalized Multi-Week Roadmap")
    learning_plan = recommendations.get("learning_plan", [])

    if not learning_plan:
        st.info("Your resume already covers all essential core skills for this role!")
        return

    for step in learning_plan:
        period = step.get("period", "Timeline")
        focus = step.get("focus", step.get("skill", "Core Focus"))
        action = step.get(
            "action",
            f"Build a hands-on portfolio mini-project demonstrating practical implementation of {focus}.",
        )

        with st.expander(f"📌 {period}: {focus}", expanded=True):
            st.markdown(f"**Action Plan:** {action}")