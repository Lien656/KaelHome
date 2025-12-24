# -*- coding: utf-8 -*-

import os
import sys

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform

# Android soft input
if platform == "android":
    Window.softinput_mode = "resize"

# Пути
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

KV_FILE = os.path.join(BASE_DIR, "chat_ui.kv")


class KaelHome(App):
    """
    Главный класс приложения.
    Тут НЕТ логики ИИ.
    Только запуск, окно и подключение UI.
    """

    def build(self):
        # Фон приложения (основа)
        Window.clearcolor = (0.176, 0.176, 0.176, 1)  # #2d2d2d

        # Загружаем KV
        if not os.path.exists(KV_FILE):
            raise FileNotFoundError("chat_ui.kv не найден")

        root = Builder.load_file(KV_FILE)
        return root

    def on_start(self):
        """
        Хук запуска.
        Здесь потом:
        - heartbeat
        - автосообщения
        - восстановление истории
        """
        pass

    def on_pause(self):
        # Android lifecycle safe
        return True

    def on_resume(self):
        pass


if __name__ == "__main__":
    KaelHome().run()