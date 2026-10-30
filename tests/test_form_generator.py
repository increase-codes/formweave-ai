import pytest

from app.form_generator import generate_form_from_text


def test_generate_form_from_recognized_labels():
    text = """
    Full Name
    Email Address
    Date of Birth
    """

    form = generate_form_from_text(text)

    assert form.title == "Generated Form"
    assert len(form.fields) == 3

    assert form.fields[0].label == "Full Name"
    assert form.fields[0].field_type == "text"

    assert form.fields[1].label == "Email Address"
    assert form.fields[1].field_type == "email"

    assert form.fields[2].label == "Date of Birth"
    assert form.fields[2].field_type == "date"


def test_unrecognized_labels_are_ignored():
    form = generate_form_from_text(
        "Favorite Color\nEmail Address"
    )

    assert len(form.fields) == 1
    assert form.fields[0].label == "Email Address"


def test_empty_text_raises_error():
    with pytest.raises(
        ValueError,
        match="Document text cannot be empty",
    ):
        generate_form_from_text("   ")


def test_no_recognized_fields_raises_error():
    with pytest.raises(
        ValueError,
        match="No recognizable form fields",
    ):
        generate_form_from_text("Favorite Color\nAddress")
