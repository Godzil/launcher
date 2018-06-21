import pygame

import config_manager as config
import skin_manager as SkinManager
import GdUI as UI

from . import top_bar
from . import screen_corners
from . import foot_bar


class MainScreen(UI.Container):
    def __init__(self, width, height):
        super().__init__(x=0, y=0, width=width, height=height)

        self._TitleBar = top_bar.TopBar(width, height)
        self._FootBar = foot_bar.FootBar(width, height)

        self._ScreenCorners = screen_corners.ScreenCorners(width, height)

        self._AppletContainer = UI.Container(x=0, y=25, width=width, height=height-25-20,
                                             bg_color=SkinManager.get_color("bgcolor"))

        self.add_child(self._AppletContainer)
        self.add_child(self._TitleBar)
        self.add_child(self._FootBar)
        self.add_child(self._ScreenCorners)

        # Border are not supported for now
        # self._FootBar.set_border(self._FootBar.borderTop, (255, 0, 0))

        self._TitleBar.set_title("GameShell")

    def reload(self):
        # Do nothing for now, later reload info from skinmanager
        pass

    def Draw(self):
        super().Draw()