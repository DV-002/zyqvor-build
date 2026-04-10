[app]
title = Zyqvorgram
package.name = zyqvorgram 
package.domain = org.zyqvor
android.p4a_whitelist
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy=2.3.0,Cython==0.29.33
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.skip_update = False
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
