import pymupdf
import pytest

from app.pdf_service import extract_text_from_pdf


def create_test_pdf(text: str) -> bytes:
    """Create a small PDF in memory for testing."""
    document = pymupdf.open()

    page = document.new_page()
    page.insert_text((72, 72), text)

    pdf_bytes = document.tobytes()
    document.close()

    return pdf_bytes


def test_extract_text_from_pdf():
    pdf_bytes = create_test_pdf("FormWeave AI test")

    extracted_text = extract_text_from_pdf(pdf_bytes)

    assert "FormWeave AI test" in extracted_text


def test_extract_text_from_multiple_pages():
    document = pymupdf.open()

    first_page = document.new_page()
    first_page.insert_text((72, 72), "First page")

    second_page = document.new_page()
    second_page.insert_text((72, 72), "Second page")

    pdf_bytes = document.tobytes()
    document.close()

    extracted_text = extract_text_from_pdf(pdf_bytes)

    assert "First page" in extracted_text
    assert "Second page" in extracted_text


def test_invalid_pdf_raises_error():
    with pytest.raises(
        ValueError,
        match="not a valid readable PDF",
    ):
        extract_text_from_pdf(b"this is not a PDF")


def test_empty_pdf_input_raises_error():
    with pytest.raises(
        ValueError,
        match="uploaded PDF is empty",
    ):
        extract_text_from_pdf(b"")
