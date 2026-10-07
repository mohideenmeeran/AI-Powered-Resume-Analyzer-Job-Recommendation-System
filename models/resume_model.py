from dataclasses import dataclass, field


@dataclass
class ResumeProfile:

    candidate_name: str = "Unknown Candidate"

    full_text: str = ""

    sections: dict = field(default_factory=dict)

    skills: list[str] = field(default_factory=list)

    resume_score: float = 0.0