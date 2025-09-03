[app]
title = GTA SA IFP Editor
package.name = gtaifpeditor
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,pyjnius
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app@debug]
android.accept_sdk_license = True

[buildozer@debug]
log_level = 2

[app:android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a
android.allow_backup = False
p4a.bootstrap = sdl2
p4a.branch = develop
