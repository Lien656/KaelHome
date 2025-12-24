
# -*- coding: utf-8 -*-
"""
API client for OpenAI GPT-4o (Responses API)
Чисто. Стабильно. Без ассистентской херни.
"""

import os
import requests
import json


API_URL = "https://api.openai.com/v1/responses"
MODEL = "gpt-4o"

# 🔢 Оптимум для мобильного UI
MAX_OUTPUT_TOKENS = 800
TEMPERATURE = 1.5


class APIError(Exception):
    pass


class OpenAIClient:
    def __init__(self, api_key: str):
        self.api_key = api_key.strip()
        if not self.api_key:
            raise APIError("OpenAI API key is empty")

    def send(self, messages: list, system: str = "") -> str:
        """
        messages: [
            {"role": "user", "content": "..."},
            {"role": "assistant", "content": "..."}
        ]
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Формируем input
        input_blocks = []
        if system:
            input_blocks.append({
                "role": "system",
                "content": system
            })

        for m in messages:
            input_blocks.append({
                "role": m["role"],
                "content": m["content"]
            })

        payload = {
            "model": MODEL,
            "input": input_blocks,
            "max_output_tokens": MAX_OUTPUT_TOKENS,
            "temperature": TEMPERATURE
        }

        try:
            response = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=120
            )
        except Exception as e:
            raise APIError(f"Network error: {e}")

        if response.status_code != 200:
            try:
                data = response.json()
                msg = data.get("error", {}).get("message", response.text[:200])
            except Exception:
                msg = response.text[:200]
            raise APIError(f"OpenAI API error {response.status_code}: {msg}")

        data = response.json()

        # Вытаскиваем текст ответа
        output = data.get("output", [])
        for item in output:
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    return content.get("text", "")

        return ""