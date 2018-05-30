# -*- coding: utf-8 -*- 

import os

import pygame

from .util_funcs import SkinMap


##pool only store surfaces

class IconPool(object):
    _GameShellIconPath = SkinMap("gameshell/icons/")
    _Icons = {}

    def __init__(self):
        self._Icons = {}

    def Init(self):

        files = os.listdir(self._GameShellIconPath)
        for i in files:
            if os.path.isfile(self._GameShellIconPath + "/" + i) and i.endswith(".png"):
                keyname = i.split(".")[0]
                self._Icons[keyname] = pygame.image.load(self._GameShellIconPath + "/" + i).convert_alpha()


MyIconPool = IconPool()
