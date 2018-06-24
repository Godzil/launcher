import pygame

import config_manager as config
import skin_manager as SkinManager
import GdUI as UI


class TopBar(UI.FlowContainer):
    def __init__(self, width, height):
        super().__init__(x=0, y=0, width=width, height=25)

        self.set_bgcolor(SkinManager.get_color("title_bg"))

        self._bottomline = UI.Widget(x=0, y=24, width=width, height=1, bg_color=SkinManager.get_color("line"))

        # Title on top
        self._TitleLbl = UI.Label(color=SkinManager.get_color("text"), font_obj=UI.FontManager.get_font("varela_16"),
                                  text="")
        self.add_left_child(self._TitleLbl)

        self.add_child(self._bottomline)

    def set_title(self, title):
        self._TitleLbl.set_text(title)

    def reload(self):
        # Do nothing for now, later reload info from skinmanager
        pass

