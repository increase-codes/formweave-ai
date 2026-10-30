from app.form_schema import FormField, FormSchema


def generate_form_from_text(text: str) -> FormSchema:
    """Convert recognizable document labels into a structured form."""

    if not text or not text.strip():
        raise ValueError("Document text cannot be empty.")

    fields = []

    for line in text.splitlines():
        label = line.strip().rstrip(":").strip()

        if not label:
            continue

        normalized = label.lower()

        if normalized in {"name", "full name", "first name", "last name"}:
            field_type = "text"
        elif "email" in normalized:
            field_type = "email"
        elif "date" in normalized or "birth" in normalized:
            field_type = "date"
        elif "phone" in normalized or "age" in normalized:
            field_type = "number"
        else:
            continue

        field_name = "_".join(normalized.split())

        fields.append(
            FormField(
                name=field_name,
                label=label,
                field_type=field_type,
                required=False,
            )
        )

    if not fields:
        raise ValueError(
            "No recognizable form fields were found in the document."
        )

    return FormSchema(
        title="Generated Form",
        fields=fields,
    )