from typing import List, Dict, Any


def generate_recommendations(job_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generates structured skill gap priorities and a multi-week actionable learning roadmap.
    """
    if not job_results:
        return {
            "skill_gaps": [],
            "learning_plan": [],
            "target_role": "General Developer",
        }

    top_role = job_results[0]
    target_role_title = top_role.get("title", "Target Role")

    missing_req = top_role.get("missing_required", [])
    missing_rec = top_role.get("missing_recommended", [])

    # Categorize Gaps into Priorities
    priority_1 = missing_req[:3]  # Learn Now
    priority_2 = missing_req[3:] + missing_rec[:2]  # Learn Next
    priority_3 = missing_rec[2:]  # Optional

    skill_gaps = [
        {
            "priority": "Priority 1 — Learn Now",
            "skills": priority_1 if priority_1 else ["Core role alignment is solid!"],
        },
        {
            "priority": "Priority 2 — Learn Next",
            "skills": priority_2 if priority_2 else ["No immediate critical secondary gaps."],
        },
        {
            "priority": "Priority 3 — Optional Boosters",
            "skills": priority_3 if priority_3 else ["Advanced optimization skills."],
        },
    ]

    # Generate Personalized Roadmap Steps
    learning_plan = []
    week_counter = 1

    if priority_1:
        for skill in priority_1:
            learning_plan.append({
                "period": f"Week {week_counter}–{week_counter+1}",
                "focus": f"Master {skill.title()}",
                "action": f"Complete hands-on tutorials and build a mini-project showcasing {skill.title()}.",
            })
            week_counter += 2

    if priority_2:
        for skill in priority_2:
            learning_plan.append({
                "period": f"Week {week_counter}",
                "focus": f"Learn {skill.title()}",
                "action": f"Integrate {skill.title()} into an existing project or dashboard in your portfolio.",
            })
            week_counter += 1

    learning_plan.append({
        "period": f"Week {week_counter}",
        "focus": "Resume Optimization & Targeted Applications",
        "action": f"Update project bullet points with measurable outcomes and apply to {target_role_title} positions.",
    })

    return {
        "target_role": target_role_title,
        "skill_gaps": skill_gaps,
        "learning_plan": learning_plan,
    }