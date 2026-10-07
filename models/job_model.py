from dataclasses import dataclass, field


@dataclass
class Job:

    title: str

    company: str

    location: str

    description: str

    skills: list[str] = field(default_factory=list)

    experience: str = ""