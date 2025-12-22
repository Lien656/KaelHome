from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import uvicorn

from memory import MemoryManager
from api_client import process_user_message

app = FastAPI()
memory = MemoryManager()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat/")
async def chat(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message")
        if not user_input:
            return JSONResponse(status_code=400, content={"error": "No message provided."})

        memory.save_message("user", user_input)
        ai_response = await process_user_message(user_input, memory)
        memory.save_message("kael", ai_response)

        return {"response": ai_response}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)