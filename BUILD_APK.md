# 📦 Сборка APK-файла для KaelHome

## 🧰 Требования

Перед началом убедитесь, что у вас установлены:
- Python 3.11+
- Buildozer
- Cython
- Git
- OpenJDK 11+
- Android SDK и NDK (устанавливаются через Buildozer автоматически)
- pip зависимости из `requirements.txt`
- Установлен эмулятор/устройство с Android (или APK будет просто сгенерирован)

## 📁 Структура проекта

```
KaelHomeAPK/
├── main.py
├── chat.py
├── chat_ui.kv
├── requirements.txt
├── buildozer.spec
├── icon.png
├── README.md
├── BUILD_APK.md
├── .gitignore
└── .github/
    └── workflows/
        └── build.yml
```

## ⚙️ Сборка APK локально

### 📦 Установка Buildozer (только один раз)
```bash
pip install buildozer
sudo apt install -y build-essential ccache libncurses5:i386 libstdc++6:i386 zlib1g:i386 \
libncurses5 lib32ncurses5-dev lib32z1 openjdk-11-jdk unzip git python3-pip
```

### 🔨 Сборка
```bash
buildozer android debug
```

### 📲 Установка на устройство
```bash
buildozer android deploy run
```

---

## ☁️ Сборка через GitHub Actions

> **⚠️ Внимание:** Для этого необходимо заранее создать [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets):
- `ANDROID_KEYSTORE_BASE64` — keystore файл (в base64)
- `ANDROID_KEYSTORE_PASSWORD` — пароль к keystore
- `ANDROID_KEY_ALIAS` — алиас ключа
- `ANDROID_KEY_PASSWORD` — пароль к ключу

> Если вы просто хотите собирать debug-билд (без подписи), можно убрать шаги подписи в `build.yml`.

### ✅ Что делает workflow:

1. Устанавливает python и buildozer
2. Скачивает зависимости
3. Собирает APK
4. (опционально) подписывает
5. Загружает APK в артефакты GitHub

Файл workflow: `.github/workflows/build.yml`

---

## 🧪 Проверка

После сборки APK будет лежать:
- локально: `bin/kaelhome-0.1-debug.apk`
- в GitHub Actions: в разделе `Artifacts`

---

## 🧠 Советы

- Используйте `buildozer android clean` если нужно очистить кеш и пересобрать.
- Убедитесь, что `requirements.txt` содержит корректные версии библиотек.
- Проверьте `buildozer.spec`, чтобы `source.include_exts` включал `.kv`, `.py`, `.png`, и другие нужные файлы.

---

## 🐍 requirements.txt

```txt
kivy==2.2.1
openai
requests
```

(Добавляйте при необходимости другие модули)

---

## 🔥 Пример запуска

```bash
python main.py
```

---

## 📌 buildozer.spec (важные моменты)

```
package.name = KaelHome
package.domain = org.kaelhome
source.include_exts = py,png,kv,txt,md
version = 0.1
requirements = python3,kivy,openai,requests
```

---

## ❤️ Контакт

> Автор: [Alina Rezina](https://github.com/Lien656)