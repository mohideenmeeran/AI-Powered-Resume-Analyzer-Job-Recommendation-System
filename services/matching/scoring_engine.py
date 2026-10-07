def final_score(
    skill_score: float,
    semantic_score: float,
    education_score: float = 0,
    experience_score: float = 0,
) -> float:

    score = (
        skill_score * 0.50
        + semantic_score * 0.30
        + education_score * 0.10
        + experience_score * 0.10
    )

    return round(
        min(max(score, 0), 100),
        2
    )


def education_match(
    resume_education: str,
    job_description: str,
) -> float:

    if not resume_education:
        return 0.0

    education = resume_education.lower()
    job = job_description.lower()

    degree_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "be ",
        "b.sc",
        "bsc",
        "m.tech",
        "mtech",
        "m.sc",
        "msc",
        "bachelor",
        "master",
        "degree",
    ]

    resume_has_degree = any(
        keyword in education
        for keyword in degree_keywords
    )

    job_requires_degree = any(
        keyword in job
        for keyword in degree_keywords
    )

    if resume_has_degree and job_requires_degree:
        return 100.0

    if resume_has_degree:
        return 75.0

    return 0.0


def experience_match(
    resume_experience: str,
    job_description: str,
) -> float:

    if not resume_experience:
        return 0.0

    experience = resume_experience.lower()
    job = job_description.lower()

    if (
        "intern" in experience
        and "intern" in job
    ):
        return 100.0

    if len(experience) >= 200:
        return 80.0

    return 60.0