# -*- coding: utf-8 -*-
"""API-клиент для OpenAI GPT"""

import requests
import json
import os

API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o"
TEMPERATURE = 1.5
MAX_TOKENS = 8192

# SSL fix для Android (опционально)
try:
    import certifi
    os.environ['SSL_CERT_FILE'] = certifi.where()
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
    SSL_VERIFY = certifi.where()
except:
    SSL_VERIFY = True


class APIError(Exception):
    pass


class OpenAI:
    """Клиент OpenAI API"""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.messages = Messages(self)
    
    def _request(self, payload):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            resp = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=180,
                verify=SSL_VERIFY
            )
        except requests.exceptions.SSLError:
            resp = requests.post(
                API_URL,
                headers=headers,
                json=payload,
                timeout=180,
                verify=False
            )
        
        if resp.status_code != 200:
            try:
                err = resp.json()
                msg = err.get('error', {}).get('message', resp.text[:200])
            except:
                msg = resp.text[:200]
            raise APIError(f"API {resp.status_code}: {msg}")
        
        return resp.json()


class Messages:
    """Интерфейс messages"""
    
    def __init__(self, client):
        self.client = client
    
    def create(self, messages, model=MODEL, system="", max_tokens=MAX_TOKENS, temperature=TEMPERATURE, **kwargs):
        if system:
            messages = [{"role": "system", "content": system}] + messages

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        data = self.client._request(payload)
        return Response(data)


class Response:
    """Ответ API"""
    
    def __init__(self, data):
        self.data = data
        self.content = [Content(data['choices'][0]['message'])]
        self.model = data.get('model', '')
        self.usage = data.get('usage', {})
        self.finish_reason = data['choices'][0].get('finish_reason', '')


class Content:
    """Контент ответа"""
    
    def __init__(self, data):
        self.type = data.get('role', 'assistant')
        self.text = data.get('content', '')