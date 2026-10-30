import streamlit as st
from pathlib import Path

from pdf_service import extract_text_from_pdf


st.set_page_config(
    page_title="FormWeave AI",
    page_icon="📄",
    layout="wide",
)

ROOT_DIR = Path(__file__).resolve().parent.parent
LOGO_PATH = ROOT_DIR / "assets" / "Form-Weave-AI Tech Emblem.png"

if LOGO_PATH.exists():
    st.image(str(LOGO_PATH), width=140)

st.title("FormWeave AI")
st.subheader("Transform PDF documents into intelligent digital forms.")

st.write("Upload a PDF to extract its text.")

uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"],
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    try:
        pdf_bytes = uploaded_file.getvalue()
        extracted_text = extract_text_from_pdf(pdf_bytes)

        if extracted_text.strip():
            st.subheader("Extracted PDF Text")
            st.text_area(
                "Review the extracted content",
                value=extracted_text,
                height=350,
            )
            st.success("PDF text extraction completed!")
        else:
            st.warning(
                "No selectable text found. "
                "This PDF may require OCR."
            )

    except Exception as error:
        st.error(f"Could not read this PDF: {error}")
