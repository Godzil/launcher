__all__ = ["Widget", "label", "image_manager", "container", "screen", "font_manager", "image", "flow_container"]

import pygame

from . import widget
from . import container
from . import label
from . import screen
from . import image
from . import flow_container

from . import font_manager as FontManager
from . import image_manager as ImageManager

Widget = widget.Widget
Label = label.Label
Container = container.Container
Screen = screen.Screen
Image = image.Image
FlowContainer = flow_container.FlowContainer

# Constant values
Width = 320
Height = 240

icon_width = 80
icon_height = 80
icon_ext = ".sh"

ICON_TYPES = {"Emulator": 7, "FILE": 6, "STAT": 5, "NAV": 4, "LETTER": 3, "FUNC": 2, "DIR": 1, "EXE": 0,
              "None": -1}  # FUNC is like UI widget's function,DIR contains child page,EXE just execute a binary

## H=horizontal, V=vertical, S=Single Line
# SLeft start from left, single line
# SCenter star from center, single line
ALIGN = {"HLeft": 0, "HCenter": 1, "HRight": 2, "VMiddle": 3, "SLeft": 4, "VCenter": 5, "SCenter": 6}
