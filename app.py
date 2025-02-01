from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import answer_question
import os

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        answer = answer_question(request.question)
        return {"question": request.question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if name == "main":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)