import requests

class APIClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def send_message(self, message):
        try:
            response = requests.post(f"{self.base_url}/chat", json={"message": message})
            if response.status_code == 200:
                return response.json().get("response", "")
            else:
                return f"[Ошибка] Код {response.status_code}: {response.text}"
        except Exception as e:
            return f"[Ошибка подключения] {e}"