from services.resume.skill_extractor import (
    extract_skills,
)


def test_skill_extraction():

    text = """
    I am a Python developer with experience
    in Pandas, SQL, Machine Learning and Power BI.
    """

    skills = extract_skills(text)

    assert "python" in skills
    assert "pandas" in skills
    assert "sql" in skills
    assert "machine learning" in skills
    assert "power bi" in skills