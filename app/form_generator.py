
import re

from app.form_schema import FormField, FormSchema


def generate_form_from_text(text: str) -> FormSchema:
    """Recognize standalone form labels despite common PDF formatting."""

    if not text or not text.strip():
        raise ValueError("Document text cannot be empty.")

    recognized_labels = {
        # Personal information
        "name": "text",
        "full name": "text",
        "applicant name": "text",
        "first name": "text",
        "last name": "text",
        "date": "date",
        "date of birth": "date",
        "age": "number",
        "email": "email",
        "email address": "email",
        "phone": "text",
        "phone number": "text",
        "contact number": "text",
        "telephone": "text",

        # Education
        "high school": "text",
        "year graduated": "number",
        "college (if applicable)": "text",
        "degree (if applicable)": "text",

        # Employment
        "previous employer": "text",
        "job title": "text",
        "duration of employment": "text",
        "reason for leaving": "textarea",

        # Other information
        "relationship": "text",
        "signature": "text",
    }

    fields = []
    seen_names = set()

    for line in text.splitlines():
        # Remove trailing spaces, underscores, and punctuation.
        label = re.sub(r"[\s_]+$", "", line.strip()).rstrip(" :-").strip()
        normalized = re.sub(r"\s+", " ", label.lower())

        # Ignore lines that are too long to be standalone field labels.
        if len(normalized) > 40:
            continue

        # Keep only recognized form labels.
        if normalized not in recognized_labels:
            continue

        # Convert labels into unique field names.
        field_name = "_".join(normalized.split())

        if field_name in seen_names:
            continue

        seen_names.add(field_name)

        fields.append(
            FormField(
                name=field_name,
                label=label,
                field_type=recognized_labels[normalized],
                required=False,
            )
        )

    if not fields:
        raise ValueError(
            "No recognizable form fields were found. "
            "This document may not be an application form."
        )

    return FormSchema(title="Generated Form", fields=fields)
