# -*- coding: utf-8 -*-

from . import font_manager
from .widget import Widget


class Label(Widget):
    def __init__(self, x=0, y=0, width=1, height=1, text="", font_obj=font_manager.get_font("default"),
                 color=(83, 83, 83), bg_color=None,
                 auto_resize=True):
        super().__init__(x=x, y=y, width=width, height=height, color=color, bg_color=bg_color)
        self._Text = text

        self._Color = color
        self._FontObj = font_obj
        self._AutoResize = auto_resize

        self._Resize()

    def _Resize(self):
        if not self._AutoResize:
            return

        tmp = self._FontObj.render(self._Text, True, self._Color)
        self.set_size(tmp.get_width(), tmp.get_height())

    def set_font(self, fontname):
        self._FontObj = font_manager.get_font(fontname)
        self._Resize()

    def get_text(self):
        return self._Text

    def set_text(self, text):
        self._Text = text
        self._Resize()

    def Draw(self):
        super().Draw()
        # Avoding same font tangling set_bold to others
        self._FontObj.set_bold(False)
        my_text = self._FontObj.render(self._Text, True, self._Color)

        self._Parent.get_canvas().blit(my_text, self._Rect)
