import pandas as pd

from config import JOBS_FILE
from models.job_model import Job


def load_jobs() -> list[Job]:

    dataframe = pd.read_csv(JOBS_FILE)

    jobs = []

    for _, row in dataframe.iterrows():

        skills = [
            skill.strip().lower()
            for skill in str(row["skills"]).split(";")
            if skill.strip()
        ]

        jobs.append(
            Job(
                title=str(row["title"]),
                company=str(row["company"]),
                location=str(row["location"]),
                description=str(row["description"]),
                skills=skills,
                experience=str(
                    row.get("experience", "")
                ),
            )
        )

    return jobs