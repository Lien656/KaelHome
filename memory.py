# -*- coding: utf-8 -*-
"""
memory.py — простая память диалога KaelHome.
Работает поверх data/chat_history.json.
Без логики ассистента. Только факты диалога.
"""

import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

MEMORY_FILE = DATA_DIR / "memory.json"


class MemoryManager:
    def __init__(self, limit: int = 500):
        self.limit = limit
        self.data = self._load()

    # ---------- IO ----------

    def _load(self):
        if not MEMORY_FILE.exists():
            return []
        try:
            return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            return []

    def _save(self):
        try:
            MEMORY_FILE.write_text(
                json.dumps(self.data[-self.limit:], ensure_ascii=False, indent=2),
                encoding="utf-8"
            )
        except Exception:
            pass

    # ---------- API ----------

    def append(self, user_text: str, kael_text: str):
        self.data.append({
            "user": user_text,
            "kael": kael_text,
            "ts": datetime.utcnow().isoformat()
        })
        self._save()

    def clear(self):
        self.data = []
        self._save()

    def all(self):
        return self.data

    def recent(self, limit: int = 20):
        return self.data[-limit:]