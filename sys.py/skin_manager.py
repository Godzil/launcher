# -*- coding: utf-8 -*-

import os
import sys
import configparser

import config
import GdUI as UI

__Colors = {}
__name = "default"
__initialized = False

__SKIN_FONT_FOLDER = "truetype"
__SKIN_IMAGE_FOLDER = "images"

__SKIN_CFG_COLORS_TAG = "Colors"
__SKIN_CFG_FONTS_TAG = "Fonts"
__SKIN_CFG_IMAGES_TAG = "Images"

def __convert_html_color(hexstr):
    h = hexstr.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def load_skin(name="default"):
    global __Colors, __name

    # Set some default values
    __Colors["background"] = (32, 32, 32)
    __Colors["high"] = (51, 166, 255)
    __Colors["text"] = (83, 83, 83)
    __Colors["front"] = (131, 199, 219)
    __Colors["url"] = (51, 166, 255)
    __Colors["line"] = (169, 169, 169)
    __Colors["title_bg"] = (228, 228, 228)
    __Colors["active"] = (175, 90, 0)
    __Colors["white"] = (255, 255, 255)

    __name = name

    # Now read from skin file
    cfg = configparser.ConfigParser()

    skin_folder = os.path.join(config.get("skinfolder"), name)

    cfgfile = os.path.join(skin_folder, "config.cfg")

    try:
        cfg.read(cfgfile)
    except Exception as e:

        if __name == "default":
            print("INTERNAL ERROR: Can't load default skin. Aborting")
            sys.exit(-1)

        # TODO: Turn that into a message box
        print("Skin configuration file for '{name}' is invalid, loading default skin".format(name=name))
        load_skin("default")
        return

    # Load skin colors
    if __SKIN_CFG_COLORS_TAG in cfg.sections():
        config_color = cfg.options(__SKIN_CFG_COLORS_TAG)

        for color in config_color:
            try:
                __Colors[color.lower()] = __convert_html_color(cfg.get(__SKIN_CFG_COLORS_TAG, color))
            except Exception:
                print("WARN: Skin '{name}': color value for '{color}' is invalid".format(name=name, color=color))

    # Load skin fonts
    if __SKIN_CFG_FONTS_TAG in cfg.sections():
        config_fonts = cfg.options(__SKIN_CFG_FONTS_TAG)

        for font in config_fonts:
            UI.FontManager.add_fontfile(font, os.path.join(skin_folder, __SKIN_FONT_FOLDER,
                                                           cfg.get(__SKIN_CFG_FONTS_TAG, font)))

    # Load skin images
    if __SKIN_CFG_IMAGES_TAG in cfg.sections():
        config_images = cfg.options(__SKIN_CFG_IMAGES_TAG)

        for image in config_images:
            UI.ImageManager.add_image(image, os.path.join(skin_folder, __SKIN_IMAGE_FOLDER,
                                                            cfg.get(__SKIN_CFG_IMAGES_TAG, image)))


def get_color(name: str):
    name = name.lower()
    if name in __Colors:
        return __Colors[name]
    else:
        print("WARN: Skin '{name}': color '{color}' does not exist".format(name=name, color=name))
        return (255, 0, 0)


if __initialized is False:
    load_skin("default")
    __initialized = True
