[app]
title = Kivy Hello World
package.name = kivyhelloworld
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# Target Android
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
