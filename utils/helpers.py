from datetime import datetime


def format_percentage(value: float) -> str:
    return f"{value:.1f}%"


def current_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def truncate_text(text: str, length: int = 250) -> str:
    if len(text) <= length:
        return text

    return text[:length].rstrip() + "..."