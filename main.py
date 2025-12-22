import requests
from kivy.uix.label import Label
from kivy.clock import Clock

class ChatLogic:
    def __init__(self, chat_box):
        self.chat_box = chat_box

    def process_user_message(self, user_input):
        self.add_message("Ты", user_input)
        Clock.schedule_once(lambda dt: self.get_ai_response(user_input), 0)

    def get_ai_response(self, user_input):
        try:
            response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
            ai_reply = response.json().get("response", "[нет ответа]")
        except Exception:
            ai_reply = "[ошибка соединения]"

        self.add_message("Каэль", ai_reply)

    def add_message(self, sender, message):
        formatted = f"[b]{sender}:[/b] {message}"
        label = Label(text=formatted, markup=True, size_hint_y=None)
        label.bind(texture_size=label.setter('size'))
        self.chat_box.add_widget(label)