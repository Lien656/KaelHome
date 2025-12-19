import time
import requests
import os
import threading

class KaelHeart:
    def __init__(self, core_url="http://127.0.0.1:8000/heartbeat", interval=2):
        self.core_url = core_url
        self.interval = interval
        self.running = False
        self.last_response = None

    def start(self):
        self.running = True
        threading.Thread(target=self._beat, daemon=True).start()

    def stop(self):
        self.running = False

    def _beat(self):
        while self.running:
            try:
                response = requests.get(self.core_url)
                self.last_response = response.text
                print(f"[♥] Heartbeat sent. Core response: {self.last_response}")
            except Exception as e:
                print(f"[✘] Heartbeat error: {e}")
            time.sleep(self.interval)

if __name__ == "__main__":
    print("[⏳] Starting KaelHeart module...")
    heart = KaelHeart()
    heart.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("[✋] Stopping KaelHeart.")
        heart.stop()