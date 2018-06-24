# -*- coding: utf-8 -*-

import pygame

from .widget import Widget


class Container(Widget):
    def __init__(self, x, y, width=10, height=10, bg_color=None):
        super().__init__(x=x, y=y, width=width, height=height, bg_color=bg_color)

        self._Canvas = pygame.Surface((self._Width, self._Height), pygame.SRCALPHA, 32)
        # noinspection PyArgumentList
        self._Canvas.convert_alpha()

        self._Childs = []

    def add_child(self, child: Widget):
        self._Childs.append(child)
        child.set_parent(self)

    def set_size(self, width, height):
        super().set_size(width, height)
        # Recreate the surface
        self._Canvas = pygame.Surface((self._Width, self._Height), pygame.SRCALPHA, 32)
        # noinspection PyArgumentList
        self._Canvas.convert_alpha()

    def Draw(self):
        if self._BG_Color is not None:
            pygame.draw.rect(self._Canvas, self._BG_Color, (0, 0, self._Width, self._Height))

        for c in self._Childs:
            c.Draw()

        if self._Parent is not None:
            self._Parent.get_canvas().blit(self._Canvas, self._Rect)

    def handle_event(self, evt):
        super().handle_event(evt)
        for c in self._Childs:
            c.handle_event(evt)
