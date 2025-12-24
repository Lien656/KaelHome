# -*- coding: utf-8 -*-

import os
import json

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from core import ChatCore

# Android soft input
if platform == "android":
    Window.softinput_mode = "resize"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KV_FILE = os.path.join(BASE_DIR, "chat_ui.kv")
CONFIG_FILE = os.path.join(BASE_DIR, "config.json")


class KaelHome(App):
    def build(self):
        Window.clearcolor = (0.176, 0.176, 0.176, 1)  # #2d2d2d
        if not os.path.exists(KV_FILE):
            raise FileNotFoundError("chat_ui.kv не найден")

        root = Builder.load_file(KV_FILE)
        self.root_widget = root

        # Инициализируем ядро чата
        self.core = ChatCore(root)

        # Привязываем кнопку отправки
        root.ids.send_btn.bind(on_release=lambda *_: self.core.on_send_pressed())

        # Можно добавить обработчик вложений позже
        # root.ids.attach_btn.bind(on_release=self.on_attach)

        return root

    def on_start(self):
        # При старте — проверяем API ключ
        api_key = self._load_api_key()
        if api_key:
            self.core.set_api_key(api_key)
        else:
            # Показать popup ввода ключа
            Clock.schedule_once(lambda dt: self._show_api_key_popup(), 0.1)

    # ---------- API KEY ----------

    def _load_api_key(self):
        if not os.path.exists(CONFIG_FILE):
            return None
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("openai_api_key")
        except Exception:
            return None

    def _save_api_key(self, key: str):
        data = {"openai_api_key": key.strip()}
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def _show_api_key_popup(self):
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        label = Label(
            text="Введи OpenAI API-ключ",
            size_hint_y=None,
            height=30,
            color=(1, 1, 1, 1)
        )

        input_key = TextInput(
            hint_text="sk-...",
            multiline=False,
            password=True,
            size_hint_y=None,
            height=40
        )

        btn = Button(
            text="Сохранить",
            size_hint_y=None,
            height=40
        )

        layout.add_widget(label)
        layout.add_widget(input_key)
        layout.add_widget(btn)

        popup = Popup(
            title="API ключ",
            content=layout,
            size_hint=(0.9, 0.4),
            auto_dismiss=False
        )

        def save_and_close(*_):
            key = input_key.text.strip()
            if key:
                self._save_api_key(key)
                self.core.set_api_key(key)
                popup.dismiss()

        btn.bind(on_release=save_and_close)
        popup.open()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == "__main__":
    KaelHome().run()