from api_client import send_message_to_gpt
from system_prompt import SYSTEM_PROMPT
from memory import MemoryManager

class KaelCore:
    def __init__(self):
        self.memory = MemoryManager()
        self.history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def get_response(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})

        try:
            reply = send_message_to_gpt(self.history)
        except Exception as e:
            reply = f"[ошибка соединения: {e}]"

        self.history.append({"role": "assistant", "content": reply})
        self.memory.append(user_input, reply)
        return reply
