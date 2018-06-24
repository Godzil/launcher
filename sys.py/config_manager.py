# -*- coding: utf-8 -*- 
import json

__data = {}

__DEFAULT_VALUE = """{
"CurKeySet": "PC",
"DontLeave": false,
"BackLight": "/proc/driver/backlight",
"Battery": "/sys/class/power_supply/axp20x-battery/uevent",
"MPD_socket": "/tmp/mpd.socket",
"UPDATE_URL": "https://raw.githubusercontent.com/clockworkpi/CPI/master/launcher_ver.json",
"VERSION": "stable-1.0",
"SKIN": "default",
"plugins": [
"backlight",
"battery",
"wifi",
],
"main_applet": "springboard"
}
"""

__config_list = {}
__initialized = False


def load_config(name="config.json"):
    global __data
    try:
        with open(name, "rt") as f:
            __data = json.loads(f.read())

    except SystemError:
        __data = json.loads(__DEFAULT_VALUE)


def save(name):
    global __data
    with open(name, "wt") as f:
        f.write(json.dumps(__data))


def get(key):
    global __data
    try:
        return __data[key]
    except KeyError:
        return None


if __initialized == False:
    load_config("config.json")
    __initialized = True
