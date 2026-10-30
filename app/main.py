
import sys
from pathlib import Path

import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.pdf_service import extract_text_from_pdf
from app.form_generator import generate_form_from_text


st.set_page_config(
    page_title="FormWeave AI",
    page_icon="📄",
    layout="wide",
)

LOGO_PATH = ROOT_DIR / "assets" / "Form-Weave-AI Tech Emblem.png"

if LOGO_PATH.exists():
    st.image(str(LOGO_PATH), width=140)

st.title("FormWeave AI")
st.subheader("Transform PDF documents into intelligent digital forms.")

st.write("Upload a PDF to extract its text and generate a structured form.")

uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"],
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    try:
        pdf_bytes = uploaded_file.getvalue()
        extracted_text = extract_text_from_pdf(pdf_bytes)3
        

        if extracted_text.strip():
            st.subheader("Extracted PDF Text")
            st.text_area(
                "Review the extracted content",
                value=extracted_text,
                height=250,
            )
            st.success("PDF text extraction completed!")

            st.subheader("Generated Form")

            try:
                form = generate_form_from_text(extracted_text)
                st.write(f"**{form.title}**")

                with st.form("generated_form"):
                    answers = {}

                    for field in form.fields:
                        if field.field_type == "textarea":
                            answers[field.name] = st.text_area(
                                field.label,
                                key=field.name,
                            )
                        elif field.field_type == "checkbox":
                            answers[field.name] = st.checkbox(
                                field.label,
                                key=field.name,
                            )
                        else:
                            answers[field.name] = st.text_input(
                                field.label,
                                key=field.name,
                            )

                    submitted = st.form_submit_button("Submit Form")

                if submitted:
                    st.subheader("Submitted Answers")
                    st.json(answers)

            except ValueError as error:
                st.warning(f"Could not generate a form: {error}")

        else:
            st.warning(
                "No selectable text found. "
                "This PDF may require OCR."
            )

    except Exception as error:
        st.error(f"Could not read this PDF: {error}")
