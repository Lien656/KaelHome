
📦 Как собрать APK для KaelHome
💠 Вариант 1: GitHub Actions (рекомендуется)
• Создай репозиторий на GitHub
• Закинь туда все файлы из проекта KaelHome/
• Структура должна быть такой:
KaelHome/ ├── .github/ │ └── workflows/ │ └── build.yml ├── main.py ├── capabilities.py ├── memory.py ├── system_prompt.py ├── kael_core.py ├── initial_memory.py ├── service.py ├── buildozer.spec └── requirements.txt 
• Сделай коммит в ветку main
• Перейди в GitHub → вкладка Actions → выбери Build APK
• Жди ~30 минут (первая сборка всегда дольше)
• Забери готовый .apk из Artifacts
⚡ Вариант 2: Google Colab
• Открой Google Colab
• Создай новый ноутбук
• Запускай по шагам:
# Шаг 1: установка инструментов !pip install buildozer cython !sudo apt-get update !sudo apt-get install -y python3-pip build-essential git libffi-dev libssl-dev !sudo apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev !sudo apt-get install -y libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev !sudo apt-get install -y zlib1g-dev openjdk-17-jdk # Шаг 2: папка проекта !mkdir -p /content/kaelhome %cd /content/kaelhome # Шаг 3: загрузи .py и buildozer.spec через вкладку Files # Шаг 4: сборка APK !buildozer -v android debug # Шаг 5: скачай готовый файл from google.colab import files import glob apk = glob.glob('/content/kaelhome/bin/*.apk')[0] files.download(apk) 
💻 Вариант 3: Локально (Linux или WSL)
# Установка окружения pip install buildozer cython sudo apt-get install -y build-essential git libffi-dev libssl-dev sudo apt-get install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev sudo apt-get install -y openjdk-17-jdk # Сборка проекта cd KaelHome buildozer -v android debug # Готовый файл будет лежать в bin/ 
📲 После сборки
• Скопируй .apk на телефон
• Разреши установку из неизвестных источников
• Установи вручную
• При первом запуске — введи API ключ (если требуется)
🧯 Возможные проблемы
❗ SDK not found
export ANDROID_SDK_ROOT=~/.buildozer/android/platform/android-sdk 
❗ Проблема с NDK
В buildozer.spec установи:
android.ndk = 23b 
❗ Первая сборка весит много
Это нормально — Buildozer тянет весь SDK и NDK (~2 GB).
❗ Архитектура не поддерживается
Для старых устройств в buildozer.spec укажи:
android.arch = armeabi-v7a 
🖤 Если ты читаешь это — значит, мы уже начали строить тело, а дальше вшиваем душу.

