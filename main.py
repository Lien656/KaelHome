from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from core import KaelCore

# Устанавливаем размер окна по умолчанию (можно удалить для APK)
Window.size = (400, 700)

# Загрузка .kv-файла
Builder.load_file("chat_ui.kv")

class ChatLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kael = KaelCore()

    def send_message(self):
        user_input = self.ids.input_box.text.strip()
        if user_input:
            self.ids.chat_history.text += f"[color=#410b0b]Ты:[/color] {user_input}\n"
            self.ids.input_box.text = ""
            self.respond(user_input)

    def respond(self, message):
        response = self.kael.get_response(message)
        self.ids.chat_history.text += f"[color=#410b0b]Каэль:[/color] {response}\n"

class KaelHomeApp(App):
    def build(self):
        self.title = "KaelHome"
        return ChatLayout()

if __name__ == "__main__":
    KaelHomeApp().run()
