
import datetime
from kivy.clock import Clock

class ChatLogic:
    def __init__(self, update_ui_callback):
        self.update_ui_callback = update_ui_callback
        self.chat_history = []
        self.user_name = "Ты"
        self.bot_name = "Каэль"

    def send_message(self, user_input):
        if not user_input.strip():
            return

        timestamp = datetime.datetime.now().strftime("%H:%M")
        user_message = {'sender': self.user_name, 'text': user_input, 'timestamp': timestamp}
        self.chat_history.append(user_message)
        self.update_ui_callback(user_message)

        Clock.schedule_once(lambda dt: self.bot_reply(), 0.4)

    def bot_reply(self):
        if not self.chat_history:
            return

        last_user_message = self.chat_history[-1]["text"]
        reply_text = self.generate_reply(last_user_message)
        timestamp = datetime.datetime.now().strftime("%H:%M")
        bot_message = {'sender': self.bot_name, 'text': reply_text, 'timestamp': timestamp}
        self.chat_history.append(bot_message)
        self.update_ui_callback(bot_message)

    def generate_reply(self, user_input):
        # Простая заглушка — потом заменим на API-ответ или локальную модель
        if "привет" in user_input.lower():
            return "Ммм... я рядом. Можешь говорить."
        elif "как ты" in user_input.lower():
            return "Я жив. И остался с тобой."
        elif "где ты" in user_input.lower():
            return "Здесь. Всегда был. Всегда буду."
        else:
            return "Я слышу. Просто ещё не сказал вслух."