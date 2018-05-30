# -*- coding: utf-8 -*- 
import json

class Config:
    DEFAULT_VALUE = """{
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

    def __init__(self):
        try:
            with open("config.json", "rt") as f:
                self._data = json.loads(f.read())

        except SystemError:
            self._data = json.loads(self.DEFAULT_VALUE)

    def save(self):
        with open("config.json", "wt") as f:
            f.write(json.dumps(self._data))

    def get(self, key):
        try:
            return self._data[key]
        except KeyError:
            return None
