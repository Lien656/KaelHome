[app]
title = KaelHome
package.name = kaelhome
package.domain = org.kael.home
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,mp3,wav,ogg,json,txt
version = 1.0.0
requirements = python3,kivy,requests,openai,plyer
orientation = portrait
fullscreen = 1
icon.filename = ./icon.png
osx.python_version = 3
osx.kivy_version = 2.1.0
presplash.filename = 
log_level = 2
entrypoint = main.py
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,FOREGROUND_SERVICE
android.api = 33
android.minapi = 24
android.ndk = 23b
android.sdk = 24
android.ndk_path = 
android.sdk_path = 
android.private_storage = true
android.hardware.accelerometer = false
android.meta_data = 
android.library_references = 
android.release_artifacts = aab,apk
android.logcat_filters = *:S python:D
android.archs = arm64-v8a,armeabi-v7a
android.gradle_dependencies = 
android.gradle_dependencies.whitelist = 

[buildozer]
log_level = 2
warn_on_root = 1