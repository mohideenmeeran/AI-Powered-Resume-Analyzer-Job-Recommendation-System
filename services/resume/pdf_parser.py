import pymupdf
from typing import Optional


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extracts structured clean text from PDF bytes using PyMuPDF.
    Preserves line breaks and document layout flow.
    Returns an empty string ("") if parsing fails or if input is empty.
    """
    if not pdf_bytes:
        return ""

    try:
        doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        if doc.page_count == 0:
            return ""

        extracted_pages = []
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            if text and text.strip():
                extracted_pages.append(text.strip())

        full_text = "\n\n".join(extracted_pages)
        return full_text.strip() if full_text.strip() else ""

    except Exception as e:
        print(f"Error reading PDF stream: {e}")
        return ""