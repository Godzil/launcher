# -*- coding: utf-8 -*-

import pygame

from .container import Container


class Screen(Container):
    def __init__(self, width=320, height=240, bg_color=(0, 0, 0), fps=30):
        # Create the actual screen first
        self._Screen = pygame.display.set_mode((width, height), 0, 32)
        self._Fps = fps
        super().__init__(x=0, y=0, width=width, height=height, bg_color=bg_color)

    def Draw(self):
        super().Draw()

        self._Screen.blit(self._Canvas, self._Rect)

        pygame.display.update()
        pygame.time.Clock().tick(self._Fps)
