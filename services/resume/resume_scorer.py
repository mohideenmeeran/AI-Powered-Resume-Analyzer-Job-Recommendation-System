import re
from typing import Dict, Any, List


def calculate_resume_score(sections: Dict[str, str], skills: List[str], full_text: str) -> Dict[str, Any]:
    """
    Computes comprehensive ATS and resume quality scores with explicit rationale.
    """
    text_lower = full_text.lower()
    
    # 1. Section Completeness (Max 25 pts)
    section_score = 0
    missing_sections = []
    present_sections = []
    
    expected_sections = {
        "summary": "Professional Summary",
        "skills": "Skills",
        "education": "Education",
        "projects": "Projects",
        "experience": "Experience/Internships",
    }
    
    for key, label in expected_sections.items():
        if key in sections and len(sections[key]) > 20:
            section_score += 5
            present_sections.append(label)
        else:
            missing_sections.append(label)

    # 2. Skill Density & Variety (Max 25 pts)
    skill_count = len(skills)
    skill_score = min(25, skill_count * 2.5)

    # 3. Quantified Achievements & Action Verbs (Max 25 pts)
    # Check for metrics (% numbers, metrics, $, X times)
    metrics_found = len(re.findall(r"\b(\d+%\b|\d+\+|\$\d+|\d+\s*x\b)", text_lower))
    metric_score = min(15, metrics_found * 3)

    action_verbs = ["built", "developed", "engineered", "designed", "implemented", "optimized", "increased", "reduced", "led", "created"]
    verb_hits = sum(1 for verb in action_verbs if re.search(rf"\b{verb}\b", text_lower))
    verb_score = min(10, verb_hits * 1.5)

    achievement_score = metric_score + verb_score

    # 4. ATS Formatting & Structure (Max 25 pts)
    ats_score = 25
    ats_issues = []

    if len(full_text) < 500:
        ats_score -= 10
        ats_issues.append("Resume content is too brief (under 500 characters).")
    if len(full_text) > 8000:
        ats_score -= 5
        ats_issues.append("Resume length exceeds standard recommended page boundaries.")
    if "@" not in text_lower:
        ats_score -= 5
        ats_issues.append("Missing explicit email contact address.")

    total_score = min(100.0, round(section_score + skill_score + achievement_score + ats_score, 1))

    # Construct Actionable Feedback
    what_is_good = []
    needs_improvement = []
    actionable_fixes = []

    if skill_count >= 8:
        what_is_good.append(f"Strong skill coverage detected ({skill_count} relevant technical/soft skills).")
    else:
        needs_improvement.append("Limited technical skill list identified.")
        actionable_fixes.append("Add core tools, frameworks, and core domain concepts to your Skills section.")

    if metrics_found >= 3:
        what_is_good.append(f"Good use of quantified outcomes ({metrics_found} metric figures found).")
    else:
        needs_improvement.append("Project descriptions lack measurable metrics and outcomes.")
        actionable_fixes.append("Incorporate concrete numbers in projects (e.g., 'Improved accuracy by 12%' or 'Processed 50k dataset entries').")

    if not missing_sections:
        what_is_good.append("All standard professional resume sections are present.")
    else:
        needs_improvement.append(f"Missing essential section(s): {', '.join(missing_sections)}.")
        actionable_fixes.append(f"Create explicit section headings for {', '.join(missing_sections)}.")

    return {
        "overall_score": total_score,
        "ats_compatibility": round((ats_score / 25) * 100, 1),
        "content_quality": round((section_score / 25) * 100, 1),
        "skill_strength": round((skill_score / 25) * 100, 1),
        "impact_strength": round((achievement_score / 25) * 100, 1),
        "what_is_good": what_is_good,
        "needs_improvement": needs_improvement,
        "actionable_fixes": actionable_fixes,
        "present_sections": present_sections,
        "missing_sections": missing_sections,
    }


def get_score_label(score_dict: Dict[str, Any]) -> str:
    """
    Returns text label for overall numerical score.
    """
    val = score_dict.get("overall_score", 0) if isinstance(score_dict, dict) else score_dict
    if val >= 85:
        return "Strong Match"
    elif val >= 70:
        return "Competitive Profile"
    elif val >= 55:
        return "Moderate Match"
    return "Needs Optimization"