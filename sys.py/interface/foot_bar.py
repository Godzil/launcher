import GdUI as UI
import skin_manager as SkinManager


class FootBar(UI.FlowContainer):
    def __init__(self, width, height):
        super().__init__(x=0, y=height - 20, width=width, height=20)

        self.set_bgcolor(SkinManager.get_color("white"))

        self._topline = UI.Widget(x=0, y=0, width=width, height=1,
                                  bg_color=SkinManager.get_color("line"))

        self.add_child(self._topline)

        self.set_margin(2)
        self.set_top_margin(1)

        self._Buttons = {"dpad": UI.Image(image=UI.ImageManager.get_sprite("buttons", 18, 18, 1)),
                         "a_key": UI.Image(image=UI.ImageManager.get_sprite("buttons", 18, 18, 4)),
                         "b_key": UI.Image(image=UI.ImageManager.get_sprite("buttons", 18, 18, 5)),
                         "x_key": UI.Image(image=UI.ImageManager.get_sprite("buttons", 18, 18, 2)),
                         "y_key": UI.Image(image=UI.ImageManager.get_sprite("buttons", 18, 18, 3))}

        self._Labels = {"dpad": UI.Label(text="", font_obj=UI.FontManager.get_font("veramono_12")),
                        "a_key": UI.Label(text="", font_obj=UI.FontManager.get_font("veramono_12")),
                        "b_key": UI.Label(text="", font_obj=UI.FontManager.get_font("veramono_12")),
                        "x_key": UI.Label(text="", font_obj=UI.FontManager.get_font("veramono_12")),
                        "y_key": UI.Label(text="", font_obj=UI.FontManager.get_font("veramono_12"))}

    def set_keyhint(self, dpad=None, a_key=None, b_key=None, x_key=None, y_key=None):
        # First clear current lists
        self.clear_left_childs()
        self.clear_right_childs()

        self._Labels["dpad"].set_text(dpad)
        self._Labels["a_key"].set_text(a_key)
        self._Labels["b_key"].set_text(b_key)
        self._Labels["x_key"].set_text(x_key)
        self._Labels["y_key"].set_text(y_key)

        if dpad is not None:
            self.add_left_child(self._Buttons["dpad"])
            self.add_left_child(self._Labels["dpad"])

        if a_key is not None:
            self.add_right_child(self._Buttons["a_key"])
            self.add_right_child(self._Labels["a_key"])

        if b_key is not None:
            self.add_right_child(self._Buttons["b_key"])
            self.add_right_child(self._Labels["b_key"])

        if x_key is not None:
            self.add_right_child(self._Buttons["x_key"])
            self.add_right_child(self._Labels["x_key"])

        if y_key is not None:
            self.add_right_child(self._Buttons["y_key"])
            self.add_right_child(self._Labels["y_key"])

    def reload(self):
        # Do nothing for now, later reload info from skinmanager
        pass
