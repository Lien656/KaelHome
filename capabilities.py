# -*- coding: utf-8 -*-
"""
Capabilities — внешние возможности KaelHome.
Без магии. Без фоновых демонов. Только то, что реально работает.
"""

import requests
from datetime import datetime


# ---------- Web ----------

def search_web(query):
    try:
        url = "https://html.duckduckgo.com/html/"
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.post(url, data={"q": query}, headers=headers, timeout=15)

        if r.status_code != 200:
            return None

        import re
        titles = re.findall(r'class="result__a"[^>]*>(.*?)<', r.text)
        snippets = re.findall(r'class="result__snippet"[^>]*>(.*?)<', r.text)

        results = []
        for i in range(min(5, len(titles), len(snippets))):
            title = re.sub(r'<.*?>', '', titles[i]).strip()
            snippet = re.sub(r'<.*?>', '', snippets[i]).strip()
            results.append(f"{title}\n{snippet}")

        return "\n\n".join(results) if results else None
    except Exception as e:
        return f"[search error: {e}]"


def fetch_webpage(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code != 200:
            return None

        import re
        text = r.text
        text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        return text[:5000]
    except Exception as e:
        return f"[fetch error: {e}]"


# ---------- Info ----------

def get_weather(city="Bishkek"):
    try:
        r = requests.get(f"https://wttr.in/{city}?format=j1", timeout=10)
        if r.status_code != 200:
            return None

        data = r.json()
        current = data.get("current_condition", [{}])[0]
        temp = current.get("temp_C", "?")
        feels = current.get("FeelsLikeC", "?")
        desc = current.get("weatherDesc", [{}])[0].get("value", "")
        return f"{temp}°C (feels {feels}°C) {desc}"
    except:
        return None


def get_time_info():
    now = datetime.now()
    return {
        "time": now.strftime("%H:%M"),
        "date": now.strftime("%Y-%m-%d"),
        "weekday": now.strftime("%A"),
        "hour": now.hour
    }


def get_wiki(topic):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{requests.utils.quote(topic)}"
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None

        data = r.json()
        title = data.get("title", topic)
        extract = data.get("extract", "")
        return f"{title}\n\n{extract}"
    except:
        return None


# ---------- Device ----------

def send_notification(title, message):
    try:
        from plyer import notification
        notification.notify(
            title=title,
            message=message[:250],
            timeout=10
        )
        return True
    except:
        return False


def vibrate(duration=0.4):
    try:
        from plyer import vibrator
        vibrator.vibrate(duration)
        return True
    except:
        return False


def copy_to_clipboard(text):
    try:
        from kivy.core.clipboard import Clipboard
        Clipboard.copy(text)
        return True
    except:
        return False


def get_clipboard():
    try:
        from kivy.core.clipboard import Clipboard
        return Clipboard.paste()
    except:
        return None


# ---------- Registry ----------

CAPABILITIES = {
    "search": search_web,
    "fetch": fetch_webpage,
    "weather": get_weather,
    "wiki": get_wiki,
    "time": get_time_info,
    "notify": send_notification,
    "vibrate": vibrate,
    "clipboard_copy": copy_to_clipboard,
    "clipboard_get": get_clipboard,
}


def execute_capability(name, *args, **kwargs):
    fn = CAPABILITIES.get(name)
    if not fn:
        return f"[unknown capability: {name}]"
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return f"[capability error {name}: {e}]"