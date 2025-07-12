from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import requests
import json
import os

print("main.py loaded")

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static frontend
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

# Store conversation
conversation_history = []

class ChatRequest(BaseModel):
    message: str

def save_history_to_file():
    with open("chatlog.json", "w", encoding="utf-8") as f:
        json.dump(conversation_history, f, ensure_ascii=False, indent=2)

def load_history_from_file():
    global conversation_history
    if os.path.exists("chatlog.json"):
        try:
            with open("chatlog.json", "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:  # try to load only if file is not empty
                    conversation_history = json.loads(content)
                else:
                    conversation_history = []
        except json.JSONDecodeError:
            print("⚠️ Warning: chatlog.json is corrupted. Starting with empty history.")
            conversation_history = []
    else:
        conversation_history = []

# Load when app starts
load_history_from_file()

@app.post("/api/chat")
async def chat(request: Request):
    body = await request.json()
    message = body.get("message")
    print("🧑‍💻 User:", message)  # <-- LOG INPUT

    global conversation_history
    conversation_history.append({"role": "user", "content": message})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "tinyllama",
            "messages": conversation_history,
            "stream": False
        }
    )

    if response.status_code == 200:
        reply = response.json()["message"]["content"]
        print("🤖 Assistant:", reply)  # <-- LOG OUTPUT

        conversation_history.append({"role": "assistant", "content": reply})
        save_history_to_file()
        return {"response": reply}

    print("❌ Error:", response.status_code, response.text)  # <-- LOG ERRORS
    return {"error": f"Error {response.status_code}: {response.text}"}

@app.get("/api/history")
def get_history():
    print("📜 Returning full conversation history")
    return {"history": conversation_history}

@app.post("/api/reset")
def reset():
    global conversation_history
    conversation_history = []
    print("🔄 Chat history reset")
    save_history_to_file()  
    return {"message": "Chat history cleared."}