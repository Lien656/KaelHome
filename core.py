# -*- coding: utf-8 -*-

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from api_client import OpenAIClient, APIError
from system_prompt import SYSTEM_PROMPT


class ChatCore:
    """
    Центральная логика чата.
    UI -> Core -> API -> UI
    """

    def __init__(self, root_widget):
        self.root = root_widget
        self.chat_box = root_widget.ids.chat_box
        self.input_field = root_widget.ids.message_input

        self.api_client = None
        self.messages = []

    # ---------- API ----------

    def set_api_key(self, api_key: str):
        self.api_client = OpenAIClient(api_key)

    # ---------- UI actions ----------

    def on_send_pressed(self):
        text = self.input_field.text.strip()
        if not text:
            return

        # Добавляем сообщение пользователя
        self._add_message(text, from_user=True)

        # Чистим поле ввода
        self.input_field.text = ""

        # Сохраняем в историю
        self.messages.append({
            "role": "user",
            "content": text
        })

        # Запрос к модели с небольшой задержкой (человечно)
        Clock.schedule_once(lambda dt: self._request_model(), 0.1)

    # ---------- Model ----------

    def _request_model(self):
        if not self.api_client:
            return

        try:
            reply = self.api_client.send(
                messages=self.messages,
                system=SYSTEM_PROMPT
            )
        except APIError as e:
            self._add_message(f"[Ошибка API]\n{e}", from_user=False)
            return

        # Возможность молчать
        if not reply or not reply.strip():
            return

        self.messages.append({
            "role": "assistant",
            "content": reply
        })

        self._add_message(reply, from_user=False)

    # ---------- Chat UI ----------

    def _add_message(self, text: str, from_user: bool):
        from kivy.factory import Factory

        bubble = Factory.ChatMessage()
        bubble.text = text

        # Цвет облачка
        if from_user:
            bubble.bg_color = (0.65, 0.65, 0.65, 0.82)  # #a6a6a6
            bubble.pos_hint = {"right": 1}
        else:
            bubble.bg_color = (0.33, 0.33, 0.33, 0.82)  # #545454
            bubble.pos_hint = {"left": 1}

        self.chat_box.add_widget(bubble)

        # Автоскролл вниз
        Clock.schedule_once(lambda dt: self._scroll_to_bottom(), 0.05)

    def _scroll_to_bottom(self):
        scroll = self.root.ids.scroll
        scroll.scroll_y = 0