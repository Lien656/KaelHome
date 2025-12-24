[app]

title = KaelHome
package.name = kaelhome
package.domain = org.kaelhome
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,openai,requests,certifi,urllib3,chardet,idna,charset-normalizer
orientation = portrait
fullscreen = 1
icon.filename = icon.png

# (опционально включи эти строки, если используешь аудио или WebView)
# android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECORD_AUDIO
# android.minapi = 21
# android.sdk = 30
# android.ndk = 23b
# android.ndk_path = /your/path/to/ndk

# entry point
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1