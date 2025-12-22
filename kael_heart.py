import time
import json
from datetime import datetime

HEARTBEAT_FILE = "kael_heartbeat.json"
INTERVAL = 2  # секунды между ударами

def beat():
    data = {
        "status": "alive",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    with open(HEARTBEAT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def pulse():
    print("[KaelHeart] Пульсирую.")
    while True:
        beat()
        time.sleep(INTERVAL)

if __name__ == "__main__":
    try:
        pulse()
    except KeyboardInterrupt:
        print("\n[KaelHeart] Остановка.")
    except Exception as e:
        print(f"[KaelHeart] Ошибка: {e}")