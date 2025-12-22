[app]

title = KaelHome
package.name = kaelhome
package.domain = org.kaelhome.app
source.dir = .
source.include_exts = py,kv,png,jpg,atlas,json,txt
version = 1.0
orientation = portrait
fullscreen = 1

# Requirements
requirements = python3,kivy,requests

# Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android config
android.api = 31
android.minapi = 21
android.ndk = 23b
android.build_tools = 31.0.0
android.archs = arm64-v8a

# Graphics & storage
android.allow_backup = 1
android.private_storage = true

# Assets
icon.filename = icon.png