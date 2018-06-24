# -*- coding: utf-8 -*-

import pygame
from .widget import Widget
from .container import Container


class FlowContainer(Container):
    def __init__(self, x, y, width=10, height=10, bg_color=None, margin=2, top_margin=2):
        super().__init__(x=x, y=y, width=width, height=height, bg_color=bg_color)

        self._LeftChilds = []
        self._RightChilds = []
        self._Margin = margin
        self._TopMargin = top_margin

    def __set_child_pos(self):
        # Left childs
        x_pos = 0
        for c in self._LeftChilds:
            x_pos += self._Margin
            c.set_position(x_pos, self._TopMargin)
            x_pos += c.get_rect().width

        # Right childs
        x_pos = self._Rect.width
        for c in reversed(self._RightChilds):
            x_pos -= c.get_rect().width
            x_pos -= self._Margin
            c.set_position(x_pos, self._TopMargin)

    def set_margin(self, margin):
        self._Margin = margin

    def set_top_margin(self, margin):
        self._TopMargin = margin

    def add_left_child(self, child: Widget):
        self._LeftChilds.append(child)
        child.set_parent(self)

    def add_right_child(self, child: Widget):
        self._RightChilds.append(child)
        child.set_parent(self)

    def clear_left_childs(self):
        self._LeftChilds.clear()

    def clear_right_childs(self):
        self._RightChilds.clear()

    def Draw(self):
        self.__set_child_pos()
        if self._BG_Color is not None:
            pygame.draw.rect(self._Canvas, self._BG_Color, (0, 0, self._Width, self._Height))

        for c in self._Childs:
            c.Draw()

        for c in self._LeftChilds:
            c.Draw()

        for c in self._RightChilds:
            c.Draw()

        self._Parent.get_canvas().blit(self._Canvas, self._Rect)

