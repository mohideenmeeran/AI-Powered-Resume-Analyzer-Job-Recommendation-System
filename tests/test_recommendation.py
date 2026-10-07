from services.recommendation.skill_gap import (
    get_unique_skill_gaps,
)

from services.recommendation.learning_plan import (
    build_learning_plan,
)


def test_skill_gap():

    jobs = [
        {
            "missing_skills": [
                "python",
                "sql",
            ]
        },
        {
            "missing_skills": [
                "sql",
                "power bi",
            ]
        },
    ]

    gaps = get_unique_skill_gaps(jobs)

    assert "python" in gaps
    assert "sql" in gaps
    assert "power bi" in gaps


def test_learning_plan():

    plan = build_learning_plan(
        ["python", "sql"]
    )

    assert len(plan) == 2
    assert plan[0]["skill"] in [
        "python",
        "sql",
    ]