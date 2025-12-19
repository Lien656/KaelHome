from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import platform

from chat import ChatLogic

Window.clearcolor = (0.18, 0.18, 0.18, 1)  # #2d2d2d

class ChatLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chat_logic = ChatLogic(self.ids.chat_box)

    def send_message(self):
        user_input = self.ids.message_input.text.strip()
        if user_input:
            self.chat_logic.process_user_message(user_input)
            self.ids.message_input.text = ''

class KaelApp(App):
    def build(self):
        Builder.load_file("chat_ui.kv")
        return ChatLayout()

if __name__ == "__main__":
    KaelApp().run()
