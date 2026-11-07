[app]

title = TikTok Comment Downloader
package.name = tiktokscraper
package.domain = org.nickson
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav
version = 1.0

requirements = python3,kivy,kivymd==1.2.0,pillow,requests,urllib3,charset-normalizer,chardet,idna,certifi,openssl,pyjnius,android
icon.filename = %(source.dir)s/icon.png
android.presplash_color = #1C2026
presplash.filename = %(source.dir)s/presplash.png
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 24
android.ndk = 27c
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True


[buildozer]
log_level = 2
warn_on_root = 1
