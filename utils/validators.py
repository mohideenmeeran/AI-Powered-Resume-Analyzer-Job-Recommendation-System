from pathlib import Path


ALLOWED_EXTENSIONS = {".pdf"}


def validate_pdf_file(file_name: str) -> bool:
    if not file_name:
        return False

    extension = Path(file_name).suffix.lower()

    return extension in ALLOWED_EXTENSIONS


def validate_resume_text(text: str) -> tuple[bool, str]:
    if not text or not text.strip():
        return False, "Resume does not contain readable text."

    if len(text.strip()) < 100:
        return False, "Resume text is too short for reliable analysis."

    return True, "Resume text is valid."