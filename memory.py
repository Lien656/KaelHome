import json
import os

MEMORY_FILE = "memory.json"

class MemoryManager:
    def __init__(self):
        self.data = []
        self.load()

    def append(self, user_input, response):
        self.data.append({"user": user_input, "kael": response})
        self.save()

    def save(self):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def load(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    self.data = []
