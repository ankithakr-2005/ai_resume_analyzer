import re
from io import BytesIO
from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file_bytes: BytesIO) -> str:
    """Extracts text from an uploaded PDF file."""
    reader = PdfReader(file_bytes)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_bytes: BytesIO) -> str:
    """Extracts text from an uploaded DOCX file."""
    doc = Document(file_bytes)
    return " ".join([p.text for p in doc.paragraphs if p.text])

def clean_text(text: str) -> str:
    """Cleans and normalizes text while preserving technical symbols like C++, C#, .NET."""
    text = text.lower()
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'[^a-z0-9\s\+#\.]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()