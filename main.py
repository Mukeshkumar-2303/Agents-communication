from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import ChatRequest
from agent import process_message

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():

    return {
        "message": "AI Agent Backend Running"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    response = process_message(
        request.session_id,
        request.message
    )

    return response