[app]

# App title shown on the phone
title = TikTok Comment Downloader

# Package name (lowercase, no spaces or hyphens)
package.name = tiktokscraper

# Package domain
package.domain = org.nickson

# Source code directory
source.dir = .

# File extensions to package into the APK (includes .wav for click.wav and .kv for main.kv)
source.include_exts = py,png,jpg,kv,atlas,wav

# App version matching your Info tab
version = 1.0

# Python & Kivy dependencies (openssl + certifi are mandatory for HTTPS requests on Android)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests,urllib3,chardet,idna,certifi,openssl,pyjnius,android

# Custom app icon
icon.filename = %(source.dir)s/icon.png

# Supported orientation
orientation = portrait

# Keep Android status/navigation bars visible
fullscreen = 0

# Android specific settings
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
