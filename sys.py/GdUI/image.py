# -*- coding: utf-8 -*-

import pygame
from .widget import Widget

class Image(Widget):
    def __init__(self, x, y, width=1, height=1, text="", bg_color=None, image=None, auto_resize=True):
        super().__init__(x=x, y=y, width=width, height=height, bg_color=bg_color)
        self._Image = image
        self._AutoResize = auto_resize
        self._Resize()

    def _Resize(self):
        if not self._AutoResize:
            return

        if self._Image is not None:
            self.set_size(self._Image.get_width(), self._Image.get_height())

    def set_image(self, image):
        self._Image = image
        self._Resize()

    def Draw(self):
        super().Draw()
        self._Parent.get_canvas().blit(self._Image, self._Rect)
