import pygame

class Widget:
    def __init__(self, parent=None, x=0, y=0, width=7, height=7):
        self._PosX = x
        self._PosY = y
        self._Width = width
        self._Height = height

        self._Color = pygame.Color(131, 199, 219)
        self._BG_Color = pygame.Color(0, 0, 0)

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
