from services.resume.pdf_parser import (
    extract_text_from_pdf,
)


def test_empty_pdf_input():

    result = extract_text_from_pdf(
        b""
    )

    assert result == ""