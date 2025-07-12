# 🤖 AI Agent Chatbot (FastAPI + Ollama + TinyLLaMA)

An interactive AI chatbot powered by [Ollama](https://ollama.com/) and TinyLLaMA, served using FastAPI, and connected to a sleek custom frontend using HTML, CSS, and JavaScript.

---

## 🧠 Features

- 💬 Chat with a local LLM (`tinyllama`) using Ollama
- 🌐 FastAPI backend with RESTful API
- 📁 Static frontend served via FastAPI
- 💾 Persistent chat history saved in `chatlog.json`
- 🔁 Reset conversation functionality
- 📜 View conversation history via endpoint

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML + CSS + JS
- **Model Runtime:** [Ollama](https://ollama.com/)
- **Model Used:** `tinyllama` (or any other compatible LLM via Ollama)
- **Others:** Pydantic, Requests, CORS, JSON

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-agent-chatbot.git
cd ai-agent-chatbot
````

### 2. Setup Python Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
```

### 3. Install Ollama and Model

Install [Ollama](https://ollama.com/) for your OS.

Then run:

```bash
ollama run tinyllama
```

> ✅ **Ensure Ollama is running in a separate terminal before starting FastAPI!**

---

### 4. Run the Backend

```bash
uvicorn main:app --reload
```

The server starts at: `http://localhost:8000`

### 📝 Sample Chat Log

This project includes a `chatlog-demo.json` file to demonstrate the structure of saved conversations.  
**Note:** Real-time chat logs are stored in `chatlog.json`, which is excluded from version control to protect user privacy.

---

### 5. Access the Frontend

Open your browser and visit:

```
http://localhost:8000/frontend/
```

You're ready to chat with your local AI! 🎉

---

## 📂 Project Structure

```
AI-agent-chatbot/
├── frontend/
│   ├── index.html
│   └── script.js
├── main.py
├── chatlog.json
├── requirements.txt
└── README.md
```

---

## 📡 API Endpoints

| Method | Endpoint       | Description                   |
| ------ | -------------- | ----------------------------- |
| POST   | `/api/chat`    | Send a message to the chatbot |
| POST   | `/api/reset`   | Clear chat history            |
| GET    | `/api/history` | Get full chat history         |

---

## 🧹 Resetting Chat

Click the **"Reset"** button in the UI or call:

```bash
curl -X POST http://localhost:8000/api/reset
```

---

## 🙋‍♀️ Made by

**Shreya H S**
Machine Learning & Cloud Enthusiast 🌙☁️🤖
Do Checkout - [Medium Post](https://medium.com/@shreyahs2004/building-a-local-ai-chatbot-using-fastapi-ollama-tinyllama-e2b6c8ba2e6f)
---

## 📄 License

This project is open-source and free to use. Modify and build upon it as needed!

```

