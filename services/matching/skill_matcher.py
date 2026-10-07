def match_skills(
    resume_skills: list[str],
    required_skills: list[str],
) -> dict:

    resume_set = {
        skill.lower().strip()
        for skill in resume_skills
    }

    required_set = {
        skill.lower().strip()
        for skill in required_skills
    }

    matched = sorted(
        resume_set & required_set
    )

    missing = sorted(
        required_set - resume_set
    )

    if not required_set:
        score = 0.0
    else:
        score = (
            len(matched)
            / len(required_set)
            * 100
        )

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "skill_score": round(score, 2),
    }