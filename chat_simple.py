# -*- coding: utf-8 -*-
"""
chat.py — логика диалога KaelHome (GPT-4o)
Не CLI. Не stream. Не ассистент.
Используется как вспомогательный модуль.
"""

import os
import json
from datetime import datetime
from pathlib import Path

from api_client import OpenAIClient, APIError
from system_prompt import SYSTEM_PROMPT


# ---------- Storage ----------

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATA_DIR / "chat_history.json"


def load_history():
    if not HISTORY_FILE.exists():
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_history(history, limit=200):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history[-limit:], f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# ---------- Chat ----------

class ChatSession:
    def __init__(self, api_key: str):
        self.client = OpenAIClient(api_key)
        self.history = load_history()

    def add(self, role: str, content: str):
        self.history.append({
            "role": role,
            "content": content,
            "ts": datetime.utcnow().isoformat()
        })
        save_history(self.history)

    def get_messages(self, limit: int = 30):
        return [
            {"role": m["role"], "content": m["content"]}
            for m in self.history[-limit:]
        ]

    def send(self, user_text: str):
        # пользователь
        self.add("user", user_text)

        try:
            reply = self.client.send(
                messages=self.get_messages(),
                system=SYSTEM_PROMPT
            )
        except APIError as e:
            return f"[API error]\n{e}"

        # возможность молчать
        if not reply or not reply.strip():
            return None

        # ответ Каэля
        self.add("assistant", reply)
        return reply