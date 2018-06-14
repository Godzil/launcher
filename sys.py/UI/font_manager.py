from . import singleton

import pygame

if not pygame.font.get_init():
    pygame.font.init()

fontpath = {}
fonts = {}


def add_fontfile(ttffile: str, name: str):
    fontpath[name] = ttffile


def get_font(fontname: str):
    try:
        return fonts[fontname]
    except IndexError:
        tok = fontname.split("_")
        fonts[fontname] = pygame.font.Font(fonts_path[tok[0]], tok[1])
        return fonts[fontname]
