[app]
title = KaelHome
package.name = kaelhome
package.domain = org.kaelhome
source.dir = .
source.include_exts = py,kv,json,png
version = 1.0
requirements = python3,kivy,openai,requests
orientation = portrait
fullscreen = 1
icon.filename = ./mipmap/iconai.png

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.permissions = INTERNET,FOREGROUND_SERVICE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.ndk = 25b
android.gradle_dependencies = 
android.ndk_path = 
android.private_storage = True
