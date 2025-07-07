from typing import Union, List, Dict, Any, Optional
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from utils.file_utils import extract_text_from_file
from utils.ai_utils import summarize_text, answer_question
from models.schemas import SummarizeRequest, SummarizeResponse, QARequest, QAResponse
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Personal Document Research Assistant API",
    description="A simple API for summarizing and answering questions about uploaded documents.",
    version="1.0.0"
)

@app.post("/upload", description="Upload a file to the API to obtain its text content.")
async def upload_file(file: UploadFile = File(...)):
    try:
        text = await extract_text_from_file(file)
        return {"text": text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/summarize", response_model=SummarizeResponse, description="Summarize the provided text.")
async def summarize(request: SummarizeRequest):
    summary = summarize_text(request.text)
    return SummarizeResponse(summary=summary)

@app.post("/ask", response_model=QAResponse, description="Answer a question about the provided text.")
async def ask(request: QARequest):
    answer = answer_question(request.text, request.question)
    return QAResponse(answer=answer)
