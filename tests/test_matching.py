from services.matching.skill_matcher import (
    match_skills,
)

from services.matching.scoring_engine import (
    final_score,
)


def test_skill_matching():

    resume_skills = [
        "python",
        "sql",
        "pandas",
    ]

    required_skills = [
        "python",
        "sql",
        "pandas",
        "power bi",
    ]

    result = match_skills(
        resume_skills,
        required_skills,
    )

    assert result["skill_score"] == 75.0

    assert "power bi" in result[
        "missing_skills"
    ]


def test_final_score():

    score = final_score(
        skill_score=80,
        semantic_score=70,
        education_score=100,
        experience_score=50,
    )

    assert score == 76.0