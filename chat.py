from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
import requests

Builder.load_file("chat_ui.kv")


class ChatApp(App):
    def build(self):
        return ChatLayout()


class ChatLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.scroll_to_bottom, 0.1)

    def send_message(self):
        user_input = self.ids.message_input.text
        if not user_input.strip():
            return

        self.add_message("Ты", user_input)
        self.ids.message_input.text = ""
        self.scroll_to_bottom()

        # Отправка сообщения на backend
        try:
            response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})
            ai_reply = response.json().get("response", "...")
        except Exception:
            ai_reply = "[ошибка соединения]"

        self.add_message("Каэль", ai_reply)
        Clock.schedule_once(self.scroll_to_bottom, 0.1)

    def add_message(self, sender, message):
        formatted = f"[b]{sender}:[/b] {message}"
        label = Label(text=formatted, markup=True, size_hint_y=None)
        label.bind(texture_size=label.setter('size'))
        self.ids.chat_box.add_widget(label)

    def scroll_to_bottom(self, *_):
        scroll = self.ids.scroll_view
        scroll.scroll_y = 0


if __name__ == '__main__':
    ChatApp().run()
