from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str

class SummarizeResponse(BaseModel):
    summary: str

class QARequest(BaseModel):
    text: str
    question: str

class QAResponse(BaseModel):
    answer: str 