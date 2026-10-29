
# FormWeave AI

FormWeave AI is a Python application that aims to transform PDF documents into structured, editable digital forms using AI.

## Current Features

- Upload PDF documents through a Streamlit interface.
- Extract selectable text from PDF pages using PyMuPDF.
- Display extracted text for review.
- Handle empty text extraction and PDF-reading errors.

## Technology Stack

- Python
- Streamlit
- PyMuPDF
- Pydantic
- OpenAI Python SDK
- python-dotenv

## Setup

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Run the application

```powershell
streamlit run app\main.py
```

## Current Limitations

- AI-powered form generation is not implemented yet.
- Scanned PDFs may require OCR.
- Extracted text may not preserve the original PDF's tables and layout.

## Project Status

Early development. Features will be added incrementally and verified before being committed to Git.
