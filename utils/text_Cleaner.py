import re


def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.replace("\x00", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s@.+#/\-]", " ", text)

    return text.strip()


def normalize_text(text: str) -> str:
    if not text:
        return ""

    text = clean_text(text)

    return text.lower().strip()


def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()

    skill = re.sub(r"\s+", " ", skill)

    return skill