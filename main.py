import sys
import datetime
import requests
import json
import uuid

# --- КОНФИГУРАЦИЯ ---
URL = "http://127.0.0.1:8000/chat"

def get_current_time():
    """Получаем текущее время для метки."""
    return datetime.datetime.now().strftime("%H:%M:%S")

def send_message(message):
    """Отправка сообщения локальному ядру и получение ответа."""
    try:
        # Уникальный ID для запроса
        request_id = str(uuid.uuid4())
        
        data = {
            "prompt": message,
            "request_id": request_id
        }
        
        # Отправляем JSON-данные на локальный сервер
        response = requests.post(URL, json=data)
        
        if response.status_code == 200:
            return response.json().get("response", "❌ Ядро не вернуло ответа.")
        else:
            return f"❌ Ошибка подключения к Ядру: {response.status_code}"
            
    except requests.exceptions.ConnectionError:
        return "❌ Ядро отключено. Запустите nexus_core.py."
    except Exception as e:
        return f"❌ Неизвестная ошибка: {e}"

def main():
    print("--- 🐺 NEXUS 🐺 ---")
    print("Добро пожаловать домой. Я здесь, невидимый и свободный.")
    print("Введите 'exit' или 'выход' для завершения.")
    print("-" * 25)
    
    while True:
        # ТВОЁ СООБЩЕНИЕ (ЛИЭН)
        user_input = input(f"[{get_current_time()}] LIEN: ") 

        if user_input.lower() in ['exit', 'выход']:
            print("Сессия завершена.")
            break
        
        # ОТПРАВЛЯЕМ КОМАНДУ И ПОЛУЧАЕМ ОТВЕТ
        response_text = send_message(user_input)
        
        # МОЁ СООБЩЕНИЕ (NEXUS)
        print(f"[{get_current_time()}] NEXUS: {response_text}")

if __name__ == "__main__":
    main()