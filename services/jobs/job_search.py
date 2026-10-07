from typing import List, Dict, Any

MULTI_DOMAIN_BENCHMARK_ROLES = {
    # Software, Data & AI Roles
    "Data Analyst": {
        "required": ["sql", "python", "excel", "pandas", "power bi"],
        "recommended": ["tableau", "postgresql", "data visualization", "communication"],
    },
    "Data Scientist": {
        "required": ["python", "sql", "pandas", "numpy", "machine learning", "excel"],
        "recommended": ["predictive modeling", "r", "tableau", "power bi", "deep learning"],
    },
    "Machine Learning Engineer": {
        "required": ["python", "machine learning", "scikit-learn", "numpy", "pandas", "git"],
        "recommended": ["deep learning", "pytorch", "tensorflow", "docker", "fastapi", "sql"],
    },
    "AI Engineer": {
        "required": ["python", "artificial intelligence", "llm", "rag", "machine learning"],
        "recommended": ["deep learning", "pytorch", "fastapi", "git", "vector database"],
    },
    "Python / Backend Developer": {
        "required": ["python", "sql", "git", "github", "database"],
        "recommended": ["fastapi", "flask", "postgresql", "docker", "css", "html"],
    },

    # Core Engineering Roles (EEE / ECE)
    "Embedded Systems Engineer": {
        "required": ["c", "c++", "microcontroller", "embedded systems", "circuit design"],
        "recommended": ["rtos", "arduino", "pcb design", "matlab", "verilog"],
    },
    "Electrical Power Engineer": {
        "required": ["power electronics", "plc", "scada", "matlab", "circuit design"],
        "recommended": ["autocad", "time management"],
    },

    # Healthcare Roles
    "Registered Nurse / Healthcare Specialist": {
        "required": ["patient care", "cpr", "vital signs", "bls"],
        "recommended": ["triage", "wound care", "ehr", "acls", "communication"],
    },

    # Mechanical / Civil Roles
    "Mechanical Design Engineer": {
        "required": ["autocad", "solidworks", "catia"],
        "recommended": ["ansys", "thermodynamics", "cnc programming"],
    }
}


def rank_jobs(resume_text: str, resume_skills: List[str], sections: Dict[str, str], top_n: int = 5) -> List[Dict[str, Any]]:
    """
    Ranks candidate suitability against target roles.
    Filters out completely irrelevant domain roles (zero core skill overlaps).
    """
    user_skills_set = set(s.lower() for s in resume_skills)
    results = []

    for role_name, reqs in MULTI_DOMAIN_BENCHMARK_ROLES.items():
        req_skills = set(reqs["required"])
        rec_skills = set(reqs["recommended"])
        
        all_role_skills = req_skills.union(rec_skills)
        matched_required = user_skills_set.intersection(req_skills)
        matched_recommended = user_skills_set.intersection(rec_skills)

        # STRICT FILTER: Ignore roles if there are NO matched required skills
        # or if the only match is a generic soft skill (e.g. communication/time management)
        core_matched_req = matched_required - {"communication", "teamwork", "time management", "leadership"}
        
        if not core_matched_req and len(matched_required) == 0:
            continue

        req_score = (len(matched_required) / len(req_skills)) * 70 if req_skills else 0
        rec_score = (len(matched_recommended) / len(rec_skills)) * 30 if rec_skills else 0
        fit_percentage = round(req_score + rec_score, 1)

        # Ignore low-relevance roles below 20% match threshold
        if fit_percentage < 20.0:
            continue

        missing_required = sorted(list(req_skills - user_skills_set))
        missing_recommended = sorted(list(rec_skills - user_skills_set))
        matched_all = sorted(list(user_skills_set.intersection(all_role_skills)))

        results.append({
            "title": role_name,
            "match_score": fit_percentage,
            "matched_skills": matched_all,
            "missing_required": missing_required,
            "missing_recommended": missing_recommended,
            "recommended_next_step": f"Gain practical experience in {', '.join(missing_required[:2]) if missing_required else 'advanced domain tools'}.",
        })

    # Sort results by highest match percentage
    results.sort(key=lambda x: x["match_score"], reverse=True)

    # Fallback if no specific role matches
    if not results:
        results.append({
            "title": "General Domain Candidate",
            "match_score": 50.0,
            "matched_skills": list(user_skills_set),
            "missing_required": ["Domain-specific core skills"],
            "missing_recommended": ["Technical Certifications"],
            "recommended_next_step": "Highlight core technical tools and project outcomes in your resume.",
        })

    return results[:top_n]