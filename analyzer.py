import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load variables from .env file
load_dotenv()

DEBUG_PROMPT = """
Analyze this ML error log:

{user_input}

Explain:
1. Possible issue
2. Why it happened
3. Suggested fixes
"""

def analyze_error(user_input: str) -> str:
    try:
        # It's better to pull the key from environment variables
        # or pass it explicitly if you prefer, but stick to "gemini-1.5-flash"
        llm = ChatGroq(
            model_name="llama-3.1-8b-instant", 
            api_key=os.getenv("GROK_API_KEY") 
        )

        prompt = PromptTemplate(
            template=DEBUG_PROMPT,
            input_variables=["user_input"]
        )

        # Using a chain is the modern LangChain way (LCEL)
        chain = prompt | llm
        
        response = chain.invoke({"user_input": user_input})
        return response.content

    except Exception as e:
        return f"Model Error: {str(e)}"
    
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

from dotenv import load_dotenv
import os

load_dotenv()

print("KEY:", os.getenv("GROK_API_KEY"))