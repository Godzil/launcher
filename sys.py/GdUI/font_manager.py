import pygame

if not pygame.font.get_init():
    pygame.font.init()

__font_files = {}
__fonts = {}
__initialized = False


def add_fontfile(name: str, ttffile: str, ):
    global __font_files
    __font_files[name] = ttffile


def __get_font_info(fontname: str):
    data = fontname.split("_")
    return data[0], int(data[1])


def set_font(asname: str, fontname: str):
    global __fonts
    try:
        __fonts[asname] = __fonts[fontname]
    except KeyError:
        fontinfo = __get_font_info(fontname)
        __fonts[fontname] = pygame.font.Font(__font_files[fontinfo[0]], fontinfo[1])
        __fonts[asname] = __fonts[fontname]


def get_font(fontname: str):
    global __fonts
    try:
        return __fonts[fontname]
    except KeyError:
        fontinfo = __get_font_info(fontname)
        try:
            __fonts[fontname] = pygame.font.Font(__font_files[fontinfo[0]], fontinfo[1])
            return __fonts[fontname]

        except KeyError:
            print("WARN: FontManager - Trying to load '{font}' but not TTF defined for it.".format(font=fontname))
            return __fonts["default"]


if __initialized is False:
    # Load default font
    add_fontfile("default", "fonts/VarelaRound-Regular.ttf")
    set_font("default", "default_12")
    __initialized = True
