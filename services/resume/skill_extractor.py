import json
import re
from typing import List, Dict, Set
from config import SKILLS_FILE


def load_skill_taxonomy() -> Dict[str, List[str]]:
    """
    Multi-domain Skill Taxonomy across IT, Non-IT, Core Engineering & Healthcare.
    """
    return {
        # IT & Software Domain
        "programming": ["python", "java", "c++", "c", "javascript", "typescript", "html", "css", "sql", "r"],
        "data_ai": ["machine learning", "deep learning", "artificial intelligence", "data science", "nlp", "rag", "llm", "predictive modeling", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "power bi", "tableau", "excel", "postgresql"],
        "tools_devops": ["git", "github", "docker", "kubernetes", "aws", "azure", "fastapi", "flask", "streamlit"],
        
        # EEE & ECE Domain
        "electrical_ece": ["circuit design", "matlab", "embedded systems", "verilog", "vlsi", "microcontroller", "arduino", "rtos", "plc", "scada", "power electronics", "iot", "signal processing", "pcb design"],
        
        # Mechanical & Civil Domain
        "mechanical_civil": ["autocad", "catia", "solidworks", "ansys", "thermodynamics", "revit", "staad pro", "cnc programming", "finite element analysis", "matlab"],
        
        # Nursing & Healthcare Domain
        "nursing_healthcare": ["patient care", "cpr", "vital signs", "phlebotomy", "ecg", "icological care", "triage", "medical records", "ehr", "pharmacology", "wound care", "bls", "acls"],
        
        # Core Soft Skills & Management
        "soft_skills": ["communication", "teamwork", "problem solving", "leadership", "time management", "critical thinking", "patient empathy"]
    }


def extract_skills(text: str) -> List[str]:
    """
    Extracts skills safely across all technical and non-technical domains using strict regex word boundaries.
    """
    if not text:
        return []

    taxonomy = load_skill_taxonomy()
    extracted: Set[str] = set()
    text_lower = text.lower()

    all_skills = []
    for category in taxonomy.values():
        if isinstance(category, list):
            all_skills.extend(category)

    for skill in all_skills:
        skill_clean = skill.strip().lower()
        if not skill_clean:
            continue

        escaped_skill = re.escape(skill_clean)
        pattern = rf"\b{escaped_skill}\b"

        if re.search(pattern, text_lower):
            extracted.add(skill_clean)

    return sorted(list(extracted))