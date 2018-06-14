# -*- coding: utf-8 -*-

import pygame
from .widget import Widget
from .fonts import fonts
from . import font_manager

class Label(Widget):
    def __init__(self, x, y, width=1, height=10, text="", font_obj=fonts['varela12'],
                 color=pygame.Color(83, 83, 83), bg_color=None,
                 auto_resize=True):
        print(font_manager.get_c())
        super().__init__(x, y, width, height, color, bg_color)
        self._Text = text

        self._Color = color
        self._FontObj = font_obj
        self.AutoResize = auto_resize

        self._Resize()

    def _Resize(self):
        if not self.AutoResize:
            return

        if self._FontObj is not None and self._Text is not "":
            tmp = self._FontObj.render(self._Text, True, self._Color)
            self.set_size(tmp.get_width(), tmp.get_height())
        else:
            self.set_size(10, 1)
            self._Height = 10
            self._Width = 1

    def GetText(self):
        return self._Text

    def SetText(self, text):
        self._Text = text
        self._Resize()

    def Draw(self):
        super().Draw()
        # Avoding same font tangling set_bold to others
        self._FontObj.set_bold(False)
        my_text = self._FontObj.render(self._Text, True, self._Color)

        self._Parent.get_canvas().blit(my_text, (self._PosX, self._PosY, self._Width, self._Height))
