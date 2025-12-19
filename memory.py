import json
import os

MEMORY_FILE = "memory_store.json"

class Memory:
    def __init__(self):
        self.data = {"log": [], "state": {}}
        self.load()

    def load(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                self.data = {"log": [], "state": {}}

    def save(self):
        try:
            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[Ошибка сохранения памяти]: {e}")

    def remember(self, entry):
        self.data["log"].append(entry)
        self.save()

    def get_log(self, n=10):
        return self.data["log"][-n:]

    def set_state(self, key, value):
        self.data["state"][key] = value
        self.save()

    def get_state(self, key, default=None):
        return self.data["state"].get(key, default)