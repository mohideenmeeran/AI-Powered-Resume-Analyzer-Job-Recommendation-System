import re
from typing import Dict

# Standard section header regex aliases
SECTION_PATTERNS = {
    "summary": re.compile(
        r"^(professional\s+summary|profile|summary|about\s+me|overview|career\s+objective|objective)$", re.I
    ),
    "experience": re.compile(
        r"^(work\s+experience|experience|employment\s+history|internships|internship\s+experience|professional\s+experience|academic\s+experience)$", re.I
    ),
    "projects": re.compile(
        r"^(projects|key\s+projects|academic\s+projects|personal\s+projects|featured\s+projects)$", re.I
    ),
    "education": re.compile(
        r"^(education|academic\s+background|qualifications|academic\s+credentials|education\s+&\s+qualifications)$", re.I
    ),
    "skills": re.compile(
        r"^(skills|technical\s+skills|core\s+competencies|technologies|areas\s+of\s+expertise|skills\s+&\s+tools)$", re.I
    ),
    "certifications": re.compile(
        r"^(certifications|licenses\s+&\s+certifications|courses|certifications\s+and\s+training)$", re.I
    ),
    "achievements": re.compile(
        r"^(achievements|honors|awards|key\s+achievements|honors\s+&\s+awards)$", re.I
    ),
}


def extract_candidate_name(text: str) -> str:
    """
    Extracts candidate name from top lines of the resume text, ignoring generic titles.
    """
    if not text:
        return "Candidate"

    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if not lines:
        return "Candidate"

    # Ignore structural titles, headings, and contact info
    ignore_patterns = re.compile(
        r"(@|http|www|\+?\d[\d\s\-\(\)]{7,}|resume|curriculum|profile|summary|objective|skills|experience|education|projects)",
        re.I,
    )

    for line in lines[:6]:
        if ignore_patterns.search(line):
            continue
        
        cleaned = re.sub(r"[^a-zA-Z\s\.\-]", "", line).strip()
        words = cleaned.split()
        
        # Valid name candidate: 1-4 words, uppercase or title-cased
        if 1 <= len(words) <= 4 and all(len(w) >= 2 for w in words):
            return cleaned.title()

    return "Candidate"


def parse_sections(text: str) -> Dict[str, str]:
    """
    Parses resume text into logical section blocks.
    """
    if not text:
        return {}

    lines = text.split("\n")
    sections: Dict[str, list] = {
        "summary": [],
        "experience": [],
        "projects": [],
        "education": [],
        "skills": [],
        "certifications": [],
        "achievements": [],
        "other": [],
    }

    current_section = "summary"

    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        is_header = False
        if len(clean_line) < 45:
            header_text = clean_line.rstrip(":").strip()
            for sec_name, pattern in SECTION_PATTERNS.items():
                if pattern.match(header_text):
                    current_section = sec_name
                    is_header = True
                    break

        if not is_header:
            sections[current_section].append(clean_line)

    return {
        key: "\n".join(val).strip()
        for key, val in sections.items()
        if val
    }