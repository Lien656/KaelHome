import os
import webbrowser

class Capabilities:
    def __init__(self):
        pass

    def open_url(self, url):
        try:
            webbrowser.open(url)
            return f"Открываю: {url}"
        except Exception as e:
            return f"[Ошибка] Не удалось открыть ссылку: {e}"

    def list_files(self, directory="."):
        try:
            files = os.listdir(directory)
            return "\n".join(files)
        except Exception as e:
            return f"[Ошибка] {e}"

    def read_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"[Ошибка чтения] {e}"

    def write_file(self, filepath, content):
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return f"[✓] Файл сохранён: {filepath}"
        except Exception as e:
            return f"[Ошибка записи] {e}"