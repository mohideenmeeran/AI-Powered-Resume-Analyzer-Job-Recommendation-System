from collections import Counter


def calculate_skill_gaps(
    job_results: list[dict],
) -> list[tuple[str, int]]:

    counter = Counter()

    for job in job_results:

        for skill in job.get(
            "missing_skills",
            [],
        ):
            counter[skill] += 1

    return counter.most_common()


def get_unique_skill_gaps(
    job_results: list[dict],
) -> list[str]:

    gaps = calculate_skill_gaps(job_results)

    return [
        skill
        for skill, _ in gaps
    ]