[app]
title = KaelHome
package.name = kaelhome
package.domain = org.kael.home

source.dir = .
source.include_exts = py,kv,png,jpg,atlas,ttf,mp3,wav,ogg,json,txt

version = 1.0.0

requirements = python3,kivy==2.3.0,requests,openai,plyer,certifi

orientation = portrait
fullscreen = 1

icon.filename = icon.png
entrypoint = main.py
log_level = 2

# ---------- Android ----------
android.api = 34
android.minapi = 28
android.archs = arm64-v8a

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,FOREGROUND_SERVICE

android.allow_backup = True
android.private_storage = True
android.enable_androidx = True
android.window_soft_input_mode = adjustResize

# Отключаем лишнее
android.hardware.accelerometer = False
android.logcat_filters = *:S python:D

# ---------- iOS / macOS (не используется, но не ломаем) ----------
osx.python_version = 3
osx.kivy_version = 2.3.0


[buildozer]
log_level = 2
warn_on_root = 1