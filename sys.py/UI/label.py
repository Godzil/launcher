# -*- coding: utf-8 -*- 

import pygame
from .widget import Widget


class Label(Widget):
    def __init__(self, x, y, width=1, height=10, parent=None, text="", font_obj=None,
                 color=pygame.Color((83, 83, 83)), bg_color=pygame.Color((0, 0, 0)),
                 auto_resize=True):
        super().__init__(x, y, width, height, color, bg_color, parent)
        self._Text = text

        self._Color = color
        self._FontObj = font_obj
        self.AutoResize = auto_resize

        self._Resize()

    def _Resize(self):
        if not self.AutoResize:
            return

        if self._FontObj is not None or self._Text is not "":
            tmp = self._FontObj.render(self._Text, True, self._Color)
            self._Width = tmp.get_width()
            self._Height = tmp.get_height()
        else:
            self._Height = 10
            self._Width = 1

    def GetText(self):
        return self._Text

    def SetText(self, text):
        self._Text = text
        self._Resize()

    def Draw(self):
        # Avoding same font tangling set_bold to others
        self._FontObj.set_bold(False)
        my_text = self._FontObj.render(self._Text, True, self._Color)

        self._CanvasHWND.blit(my_text, (self._PosX, self._PosY, self._Width, self._Height))
