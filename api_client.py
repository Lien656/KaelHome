import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY") or "sk-ТО_ЧТО_ТЫ_ВСТАВИШЬ"

MODEL = "gpt-4o"
TEMPERATURE = 1.5


def send_message_to_gpt(history):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=history,
        temperature=TEMPERATURE,
        top_p=1.0,
        presence_penalty=1.0,
        frequency_penalty=0.25,
    )

    return response.choices[0].message.content.strip()
