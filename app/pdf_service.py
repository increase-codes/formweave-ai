
import pymupdf


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract selectable text from PDF bytes."""

    if not pdf_bytes:
        raise ValueError("The uploaded PDF is empty.")

    try:
        with pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf",
        ) as pdf:
            return "\n".join(
                page.get_text() for page in pdf
            )

    except (pymupdf.FileDataError, pymupdf.EmptyFileError) as error:
        raise ValueError(
            "The uploaded file is not a valid readable PDF."
        ) from error
