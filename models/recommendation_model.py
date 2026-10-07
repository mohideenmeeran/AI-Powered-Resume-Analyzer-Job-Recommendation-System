from dataclasses import dataclass, field


@dataclass
class Recommendation:

    skill_gaps: list[str] = field(default_factory=list)

    learning_plan: list[dict] = field(default_factory=list)