# -*- coding: utf-8 -*-
"""
kael_heart.py — heartbeat Каэля.
Тихий пульс. Даже когда чат молчит.
"""

import time
import json
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

HEARTBEAT_FILE = DATA_DIR / "kael_heartbeat.json"
INTERVAL = 2.0  # секунды между ударами


def beat():
    data = {
        "status": "alive",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    try:
        with open(HEARTBEAT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def pulse():
    while True:
        beat()
        time.sleep(INTERVAL)


if __name__ == "__main__":
    try:
        pulse()
    except KeyboardInterrupt:
        pass