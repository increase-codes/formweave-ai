
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class FormField(BaseModel):
    name: str = Field(min_length=1)
    label: str = Field(min_length=1)
    field_type: Literal[
        "text",
        "email",
        "number",
        "date",
        "select",
        "checkbox",
        "textarea",
    ]
    required: bool = False
    options: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_options(self):
        if self.field_type == "select" and not self.options:
            raise ValueError(
                "Select fields must have at least one option."
            )

        if self.field_type != "select" and self.options:
            raise ValueError(
                "Only select fields can have options."
            )

        return self


class FormSchema(BaseModel):
    title: str = Field(min_length=1)
    fields: list[FormField] = Field(min_length=1)
