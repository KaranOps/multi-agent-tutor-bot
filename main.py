# main.py
print("🚀 FastAPI App is starting...")

from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from tutor_agent.agent import root_agent  
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Instantiate FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask(request: Request, question: str = Form(None)):
    """
    POST endpoint to handle user questions.
    Supports both form-encoded and JSON inputs.
    """
    if question is None:
        try:
            data = await request.json()
            question = data.get("question", "")
        except Exception:
            return JSONResponse(content={"error": "Invalid input"}, status_code=400)

    if not question:
        return JSONResponse(content={"error": "Question is required"}, status_code=400)

    try:
        response = root_agent.invoke({"input": question}, config={"env": {"GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY")}})
        return JSONResponse(content={"answer": response["output"]})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
async def serve_homepage():
    return FileResponse("templates/index.html")
