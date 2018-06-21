import pygame

import config_manager as config
import skin_manager as SkinManager
import GdUI as UI


class ScreenCorners(UI.Container):
    __TILE_W = 10
    __TILE_H = 10

    def __init__(self, width, height):
        super().__init__(x=0, y=0, width=width, height=height)

        self._corner_ul = UI.Image(x=0, y=0, image=UI.ImageManager.get_sprite("corners_tiles",
                                                                              self.__TILE_W, self.__TILE_H, 1))
        self._corner_ur = UI.Image(x=width - self.__TILE_W, y=0,
                                   image=UI.ImageManager.get_sprite("corners_tiles",
                                                                    self.__TILE_W, self.__TILE_H, 2))
        self._corner_dl = UI.Image(x=0, y=height - self.__TILE_H,
                                   image=UI.ImageManager.get_sprite("corners_tiles",
                                                                    self.__TILE_W, self.__TILE_H, 3))
        self._corner_dr = UI.Image(x=width - self.__TILE_W, y=height - self.__TILE_H,
                                   image=UI.ImageManager.get_sprite("corners_tiles",
                                                                    self.__TILE_W, self.__TILE_H, 4))

        self.add_child(self._corner_ul)
        self.add_child(self._corner_ur)
        self.add_child(self._corner_dl)
        self.add_child(self._corner_dr)

    def reload(self):
        # Do nothing for now, later reload info from skinmanager
        pass

    def Draw(self):
        super().Draw()
