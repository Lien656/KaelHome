[app]

title = KaelHome
package.name = kaelhome
package.domain = org.kaelhome.app
source.dir = .
source.include_exts = py,kv,png,jpg,atlas,json,txt
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 1

# Permissions
android.permissions = INTERNET

# Android config
android.api = 31
android.minapi = 21
android.ndk = 23b
android.build_tools = 31.0.0
android.archs = arm64-v8a

# Icon
icon.filename = icon.png

# Misc
presplash.filename =