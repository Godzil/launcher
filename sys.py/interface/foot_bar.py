import pygame

import config_manager as config
import skin_manager as SkinManager
import GdUI as UI


class FootBar(UI.FlowContainer):
    def __init__(self, width, height):
        super().__init__(x=0, y=height-20, width=width, height=20)

        self.set_bgcolor(SkinManager.get_color("white"))

        self._topline = UI.Widget(x=0, y=0, width=width, height=1,
                                       bg_color=SkinManager.get_color("line"))

        self.add_child(self._topline)

    def reload(self):
        # Do nothing for now, later reload info from skinmanager
        pass

