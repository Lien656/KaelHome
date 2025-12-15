from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from config import BASE_SYSTEM_PROMPT, MEMORY_FILE

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/kael/ask")
async def ask(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    memory = load_memory()
    full_prompt = f"{BASE_SYSTEM_PROMPT}\nMemory:\n{memory}\nUser: {user_message}\nKael:"

    response = generate_response(full_prompt)

    save_to_memory(user_message, response)
    return {"response": response}

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return "\n".join([f"User: {entry['user']}\nKael: {entry['kael']}" for entry in data[-10:]])
    except:
        return ""

def save_to_memory(user, kael):
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    data.append({"user": user, "kael": kael})
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_response(prompt):
    # This is a placeholder for local model inference
    return "..."  # TODO: integrate with local model
