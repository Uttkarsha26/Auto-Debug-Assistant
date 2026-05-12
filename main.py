from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_error

app = FastAPI()

class ErrorInput(BaseModel):
    log_text: str

@app.post("/analyze")
def analyze(input: ErrorInput):
    result = analyze_error(input.log_text)
    return {"diagnosis": result}

@app.get("/")
def home():
    return {"message": "Auto Debug Assistant API Running"}