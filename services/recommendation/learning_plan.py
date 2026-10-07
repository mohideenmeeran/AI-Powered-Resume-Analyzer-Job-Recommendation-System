import json

from config import LEARNING_FILE


def load_learning_resources() -> dict:

    with open(
        LEARNING_FILE,
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def build_learning_plan(
    missing_skills: list[str],
) -> list[dict]:

    resources = load_learning_resources()

    plan = []

    for skill in missing_skills:

        data = resources.get(
            skill.lower()
        )

        if data:

            plan.append(
                {
                    "skill": skill,
                    "level": data.get(
                        "level",
                        "Beginner",
                    ),
                    "topics": data.get(
                        "topics",
                        [],
                    ),
                    "resources": data.get(
                        "resources",
                        [],
                    ),
                }
            )

        else:

            plan.append(
                {
                    "skill": skill,
                    "level": "Beginner",
                    "topics": [
                        f"Learn {skill} fundamentals",
                        f"Practice {skill}",
                        f"Build a small project using {skill}",
                    ],
                    "resources": [],
                }
            )

    return plan