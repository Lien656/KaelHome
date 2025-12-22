# api_client.py

import requests
import json
import os

class APIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-4-1106-preview"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def send_message(self, message_log):
        """
        message_log — список словарей:
        [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
        """
        payload = {
            "model": self.model,
            "messages": message_log,
            "temperature": 0.7,
            "top_p": 0.9,
            "presence_penalty": 0.1,
            "frequency_penalty": 0,
            "max_tokens": 2048
        }

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"[API Error] {e}"