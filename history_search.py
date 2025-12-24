# -*- coding: utf-8 -*-
"""
Поиск по истории KaelHome.
Простой, быстрый, локальный.
"""

import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
HISTORY_FILE = DATA_DIR / "chat_history.json"


def search(query: str, limit: int = 20):
    if not HISTORY_FILE.exists():
        return []

    try:
        data = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

    q = query.lower().strip()
    if not q:
        return []

    results = []
    for msg in reversed(data):
        content = msg.get("content", "")
        if q in content.lower():
            results.append(msg)
            if len(results) >= limit:
                break

    return results