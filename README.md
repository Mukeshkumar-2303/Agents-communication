# AI Agent Communication System

A simple AI Agent Communication System built using React.js and FastAPI.

This project demonstrates multi-agent interaction between a Frontend Agent and a Backend Agent through a chat-style interface.

---

# Features

- User task input
- Frontend Agent communication
- Backend Agent processing
- Multi-step agent interaction
- Clarification questions
- Final content generation
- Chat-style UI
- FastAPI REST API integration

---

# Tech Stack

## Frontend
- React.js
- Vite
- Axios

## Backend
- FastAPI
- Python
- Uvicorn

---

# Project Structure

```text
ai-agent-system/
│
├── frontend/
│   ├── src/
│   ├── package.json
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── memory.py
│   ├── models.py
│   ├── utils.py
│   ├── requirements.txt
│
└── README.md
---
Backend Setup
Step 1 → Go to backend folder
cd backend
Step 2 → Create virtual environment
python -m venv venv
Step 3 → Activate virtual environment
Windows
venv\Scripts\activate
Step 4 → Install dependencies
pip install -r requirements.txt
Step 5 → Run backend server
uvicorn main:app --reload

Backend runs on:

http://localhost:8000
Frontend Setup
Step 1 → Go to frontend folder
cd frontend
Step 2 → Install dependencies
npm install
Step 3 → Install axios
npm install axios
Step 4 → Run frontend
npm run dev

Frontend runs on:

http://localhost:5173
Example Workflow

User enters a task:

Create a short blog about AI in hiring

Frontend Agent sends request to Backend Agent.

Backend Agent asks:

tone
length

After collecting details, Backend Agent generates the final output.

Example Interaction
User:
Create a short blog about AI in hiring

Backend Agent:
What tone would you like? (formal/casual)

User:
formal

Backend Agent:
What length should the content be? (short/medium)

User:
short

Backend Agent:
Generates final content
