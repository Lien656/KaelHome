# -*- coding: utf-8 -*-
"""
Локальное хранилище памяти и истории.
Надёжно, просто, без лишней магии.
"""

import os
import json
from datetime import datetime
from pathlib import Path


APP_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = APP_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATA_DIR / "chat_history.json"


class MemoryStore:
    def __init__(self, max_items: int = 500):
        self.max_items = max_items
        self.history = self._load()

    # ---------- IO ----------

    def _load(self):
        if not HISTORY_FILE.exists():
            return []
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _save(self):
        try:
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.history[-self.max_items:], f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    # ---------- API ----------

    def add(self, role: str, content: str):
        self.history.append({
            "role": role,
            "content": content,
            "ts": datetime.utcnow().isoformat()
        })
        self._save()

    def clear(self):
        self.history = []
        self._save()

    def get_recent(self, limit: int = 50):
        return self.history[-limit:]

    def all(self):
        return self.history