import pygame

class Widget:
    def __init__(self, x=0, y=0, width=7, height=7,
                 color=pygame.Color((131, 199, 219)),
                 bg_color= pygame.Color((0, 0, 0)),
                 parent=None):
        self._PosX = x
        self._PosY = y
        self._Width = width
        self._Height = height

        self._Color = color
        self._BG_Color = bg_color

        self._Parent = parent

        if self._Parent is not None:
            self._CanvasHWND = parent.CanvasHWND

    def SetCanvasHWND(self, canvas):
        self._CanvasHWND = canvas

    def set_position(self, x, y):
        self._PosX = x
        self._PosY = y

    def set_size(self, width, height):
        self._Height = height
        self._Width = width

    def set_color(self, color):
        self._Color = color

    def set_bgcolor(self, color):
        self._BG_Color = color

    def Draw(self):
        pass
