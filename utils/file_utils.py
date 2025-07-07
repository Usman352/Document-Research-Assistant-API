import io
import PyPDF2
from fastapi import UploadFile

async def extract_text_from_file(file: UploadFile) -> str:
    if file.content_type == 'application/pdf' or (file.filename and file.filename.lower().endswith('.pdf')):
        file_content = await file.read()
        reader = PyPDF2.PdfReader(io.BytesIO(file_content))
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    elif file.content_type == 'text/plain' or (file.filename and file.filename.lower().endswith('.txt')):
        contents = await file.read()
        return contents.decode('utf-8')
    else:
        raise ValueError('Unsupported file type. Only PDF and TXT are supported.') 