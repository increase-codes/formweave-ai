
import pytest
from pydantic import ValidationError

from app.form_schema import FormField, FormSchema


def test_valid_form_schema():
    form = FormSchema(
        title="Registration Form",
        fields=[
            FormField(
                name="email",
                label="Email Address",
                field_type="email",
                required=True,
            ),
            FormField(
                name="country",
                label="Country",
                field_type="select",
                options=["Nigeria", "Ghana"],
            ),
        ],
    )

    assert form.title == "Registration Form"
    assert len(form.fields) == 2


def test_select_requires_options():
    with pytest.raises(
        ValidationError,
        match="Select fields must have at least one option",
    ):
        FormField(
            name="country",
            label="Country",
            field_type="select",
        )


def test_non_select_cannot_have_options():
    with pytest.raises(
        ValidationError,
        match="Only select fields can have options",
    ):
        FormField(
            name="email",
            label="Email",
            field_type="email",
            options=["Option A"],
        )


def test_form_requires_at_least_one_field():
    with pytest.raises(ValidationError):
        FormSchema(title="Empty Form", fields=[])
