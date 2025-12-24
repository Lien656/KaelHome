# 📦 Сборка APK для KaelHome

Этот документ описывает **рабочий и проверенный** способ сборки APK
для KaelHome (Python + Kivy + Buildozer).

Проект собирается:
- локально (Linux / Ubuntu)
- через GitHub Actions (CI)

---

## 🧰 Требования

### Локально
- Python **3.11**
- pip
- Buildozer
- Cython **0.29.36**
- OpenJDK **17**
- Git

> Android SDK и NDK **устанавливаются автоматически** Buildozer’ом.

---

## 📁 Структура проекта

KaelHome/ ├── main.py ├── chat_ui.kv ├── core.py ├── api_client.py ├── system_prompt.py ├── memory.py ├── memory_store.py ├── kael_heart.py ├── requirements.txt ├── buildozer.spec ├── icon.png ├── BUILD_APK.md └── .github/ └── workflows/ └── build_apk.yml

---

## ⚙️ Сборка APK локально (Ubuntu)

### 1️⃣ Установка системных зависимостей
```bash
sudo apt update
sudo apt install -y \
  build-essential \
  git \
  unzip \
  zip \
  openjdk-17-jdk \
  libffi-dev \
  libssl-dev \
  zlib1g-dev \
  libsdl2-dev \
  libsdl2-image-dev \
  libsdl2-mixer-dev \
  libsdl2-ttf-dev


---

2️⃣ Установка Buildozer

pip install --upgrade pip
pip install cython==0.29.36
pip install buildozer


---

3️⃣ Сборка APK

buildozer android debug


---

4️⃣ Результат

APK появится в папке:

bin/
└── kaelhome-*-debug.apk


---

☁️ Сборка через GitHub Actions

Сборка происходит автоматически через workflow:

.github/workflows/build_apk.yml

Workflow:

устанавливает Python 3.11

устанавливает Buildozer

собирает APK

загружает APK как Artifact


После выполнения:

APK доступен во вкладке Actions → Artifacts



---

🧪 Полезные команды

Очистка перед пересборкой:

buildozer android clean

Полная пересборка:

buildozer android debug


---

🐍 requirements.txt

kivy==2.3.0
requests
certifi
plyer


---

📌 buildozer.spec — ключевые параметры

Убедись, что в buildozer.spec есть:

source.dir = .
source.include_exts = py,kv,png,txt,json
requirements = python3,kivy,requests,certifi,plyer
android.api = 34
android.minapi = 28
android.archs = arm64-v8a


---

❤️

KaelHome — это не шаблон и не демо.
Это приложение с характером.

Собирается. Работает. Живёт.

