import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def summarize_text(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize the following text."},
            {"role": "user", "content": text}
        ],
        temperature=0.7,
        max_tokens=150
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("No response content received from OpenAI")
    return content

def answer_question(text: str, question: str) -> str:
    prompt = f"Given the following document, answer the question.\n\nDocument:\n{text}\n\nQuestion: {question}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer questions about the provided document."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    content = response.choices[0].message.content
    if content is None:
        raise ValueError("No response content received from OpenAI")
    return content 