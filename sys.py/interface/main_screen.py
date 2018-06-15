import pygame

import config_manager as config
import skin_manager as SkinManager
import GdUI as UI


class MainScreen(UI.Container):
    def __init__(self, width, height):
        super().__init__(x=0, y=0, width=width, height=height)

        self._TitleBar = UI.FlowContainer(x=0, y=0, width=width, height=25)
        self._TitleBar.set_bgcolor(SkinManager.get_color("title_bg"))

        self._TitleBar_line = UI.Widget(x=0, y=24, width=width, height=1,
                                       bg_color=SkinManager.get_color("line"))

        self._FootBar = UI.FlowContainer(x=0, y=height - 20, width=width, height=20)
        self._FootBar.set_bgcolor(SkinManager.get_color("white"))

        self._FootBar_line = UI.Widget(x=0, y=0, width=width, height=1,
                                       bg_color=SkinManager.get_color("line"))

        self._AppletContainer = UI.Container(x=0, y=25, width=width, height=height-25-20,
                                             bg_color=SkinManager.get_color("bgcolor"))

        self._corner_ul = UI.Image(x=0, y=0, image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 1))
        self._corner_ur = UI.Image(x=width - 10, y=0,
                                   image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 2))
        self._corner_dl = UI.Image(x=0, y=height - 10,
                                   image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 3))
        self._corner_dr = UI.Image(x=width - 10, y=height - 10,
                                   image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 4))

        self.add_child(self._TitleBar)
        self.add_child(self._FootBar)
        self._FootBar.add_child(self._FootBar_line)
        self._TitleBar.add_child(self._TitleBar_line)
        self.add_child(self._AppletContainer)
        self.add_child(self._corner_ul)
        self.add_child(self._corner_ur)
        self.add_child(self._corner_dl)
        self.add_child(self._corner_dr)

        # Title on top
        self._Title = "GameShell"
        self._TitleLbl = UI.Label(color=SkinManager.get_color("text"), font_obj=UI.FontManager.get_font("varela_16"),
                                  text=self._Title)
        self._TitleBar.add_left_child(self._TitleLbl)

    def reload(self):
        # Do nothing for now, later reload info from skinmanager
        pass

