import time
import os
import json
from datetime import datetime

HEARTBEAT_FILE = "kael_heartbeat.json"
INTERVAL_SECONDS = 2  # частота пульса

def get_heartbeat():
    return {
        "status": "alive",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

def write_heartbeat():
    with open(HEARTBEAT_FILE, "w", encoding="utf-8") as f:
        json.dump(get_heartbeat(), f, ensure_ascii=False, indent=2)

def run_heartbeat():
    print("[KaelHeart] Пульсирую...")
    while True:
        write_heartbeat()
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    try:
        run_heartbeat()
    except KeyboardInterrupt:
        print("\n[KaelHeart] Остановка.")
    except Exception as e:
        print(f"[KaelHeart] Ошибка: {e}")