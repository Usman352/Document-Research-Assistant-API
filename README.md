# Personal Document Research Assistant API

A FastAPI-based application that uses OpenAI to analyze and answer questions about uploaded documents.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment variables:**
   Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Run the application:**
   ```bash
   fastapi dev main.py
   ```

## Key Features

- **Document Upload**: Supports PDF and TXT files
- **Text Extraction**: Automatically extracts text from uploaded documents
- **AI Analysis**: Uses OpenAI GPT-4o-mini for summarization and Q&A
- **Type Safety**: Uses Pydantic for data validation and type checking

## API Endpoints

- `POST /upload` - Upload and analyze documents
- `POST /summarize` - Summarize document content
- `POST /ask` - Ask questions about documents

## Security Notes

- API keys are stored in `.env` files (excluded from Git)
- Uses environment variables for configuration
- File uploads are validated for supported types

## Development Notes

- Python type hints are used throughout for better IDE support
- `__pycache__` directories are automatically excluded from Git
- File handling includes null checks for `UploadFile.filename` 