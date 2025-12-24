# -*- coding: utf-8 -*-

from kivy.clock import Clock
from kivy.factory import Factory

from api_client import OpenAIClient, APIError
from system_prompt import SYSTEM_PROMPT
from memory_store import MemoryStore


class ChatCore:
    """
    Центральная логика чата KaelHome.
    UI -> Core -> API -> Memory -> UI
    """

    def __init__(self, root_widget):
        self.root = root_widget
        self.chat_box = root_widget.ids.chat_box
        self.input_field = root_widget.ids.message_input

        self.api_client = None

        # Память
        self.memory = MemoryStore(max_items=500)
        self.messages = self.memory.get_recent(limit=30)

        # При старте — восстановить историю в UI
        Clock.schedule_once(lambda dt: self._restore_history(), 0)

    # ---------- API ----------

    def set_api_key(self, api_key: str):
        self.api_client = OpenAIClient(api_key)

    # ---------- UI actions ----------

    def on_send_pressed(self):
        text = self.input_field.text.strip()
        if not text:
            return

        self.input_field.text = ""

        # UI
        self._add_message(text, from_user=True)

        # Память
        self.memory.add("user", text)
        self.messages.append({"role": "user", "content": text})

        # Запрос к модели
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
            self._add_message(f"[API error]\n{e}", from_user=False)
            return

        # Возможность молчать
        if not reply or not reply.strip():
            return

        # Память
        self.memory.add("assistant", reply)
        self.messages.append({"role": "assistant", "content": reply})

        # UI
        self._add_message(reply, from_user=False)

    # ---------- History ----------

    def _restore_history(self):
        for msg in self.messages:
            role = msg.get("role")
            content = msg.get("content", "")
            if role == "user":
                self._add_message(content, from_user=True, scroll=False)
            elif role == "assistant":
                self._add_message(content, from_user=False, scroll=False)

        self._scroll_to_bottom()

    # ---------- Chat UI ----------

    def _add_message(self, text: str, from_user: bool, scroll: bool = True):
        bubble = Factory.ChatMessage()
        bubble.text = text

        if from_user:
            bubble.bg_color = (0.65, 0.65, 0.65, 0.82)  # #a6a6a6
            bubble.pos_hint = {"right": 1}
        else:
            bubble.bg_color = (0.33, 0.33, 0.33, 0.82)  # #545454
            bubble.pos_hint = {"left": 1}

        self.chat_box.add_widget(bubble)

        if scroll:
            Clock.schedule_once(lambda dt: self._scroll_to_bottom(), 0.05)

    def _scroll_to_bottom(self):
        scroll = self.root.ids.scroll
        scroll.scroll_y = 0