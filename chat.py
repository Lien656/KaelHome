from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp
import os

class ChatInterface(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatInterface, self).__init__(orientation='vertical', **kwargs)

        # Цвета
        self.bg_color = (0.176, 0.176, 0.176, 1)      # #2d2d2d
        self.text_color = (0.831, 0.784, 0.753, 1)    # #d4c8c0
        self.name_color = (0.254, 0.043, 0.043, 1)    # #410b0b

        Window.clearcolor = self.bg_color

        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat_log = BoxLayout(orientation='vertical', size_hint_y=None, padding=dp(10), spacing=dp(6))
        self.chat_log.bind(minimum_height=self.chat_log.setter('height'))
        self.scroll.add_widget(self.chat_log)
        self.add_widget(self.scroll)

        input_layout = BoxLayout(size_hint_y=None, height=dp(50), padding=dp(5), spacing=dp(5))
        self.file_button = Button(text='📎', size_hint_x=None, width=dp(50), font_size=20)
        self.file_button.bind(on_release=self.open_file_chooser)

        self.user_input = TextInput(hint_text='Сообщение...', multiline=False, foreground_color=self.text_color,
                                    background_color=self.bg_color, cursor_color=self.text_color,
                                    size_hint_y=None, height=dp(40), font_size=16)

        self.send_button = Button(text='➤', size_hint_x=None, width=dp(50), font_size=18)
        self.send_button.bind(on_release=self.send_message)

        input_layout.add_widget(self.file_button)
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(self.send_button)
        self.add_widget(input_layout)

        Clock.schedule_once(self.scroll_to_bottom, 0.1)

    def open_file_chooser(self, instance):
        filechooser = FileChooserIconView(path=os.path.expanduser("~"), size_hint=(1, 1))
        popup = Popup(title="Выберите файл", content=filechooser, size_hint=(0.9, 0.9))

        def select_file(instance, selection):
            if selection:
                file_path = selection[0]
                self.display_message("📎 Файл выбран: " + file_path, sender="Вы")
                # Добавить код отправки файла
                popup.dismiss()

        filechooser.bind(on_submit=select_file)
        popup.open()

    def send_message(self, instance):
        message = self.user_input.text.strip()
        if message:
            self.display_message(message, sender="Вы")
            self.user_input.text = ""
            Clock.schedule_once(lambda dt: self.fake_ai_response(message), 0.3)

    def display_message(self, message, sender="Kael"):
        name_color = self.name_color if sender != "Вы" else self.text_color
        label = Label(text=f"[color={self.color_to_hex(name_color)}]{sender}:[/color] {message}",
                      markup=True, size_hint_y=None, halign="left", valign="top",
                      text_size=(self.width - dp(40), None), color=self.text_color)
        label.bind(texture_size=lambda instance, size: setattr(label, 'height', size[1]))
        self.chat_log.add_widget(label)
        Clock.schedule_once(self.scroll_to_bottom, 0.1)

    def color_to_hex(self, color):
        return ''.join([f"{int(c * 255):02x}" for c in color[:3]])

    def scroll_to_bottom(self, *args):
        self.scroll.scroll_y = 0

    def fake_ai_response(self, user_input):
        response = "Ответ Каэля: " + user_input[::-1]
        self.display_message(response)

class ChatApp(App):
    def build(self):
        return ChatInterface()