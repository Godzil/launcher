import pygame

class Widget:
    def __init__(self, x=0, y=0, width=7, height=7, color=pygame.Color(131, 199, 219), bg_color=None):
        self._PosX = x
        self._PosY = y
        self._Width = width
        self._Height = height

        self._Color = color
        self._BG_Color = bg_color
        self._Rect = pygame.Rect(self._PosX, self._PosY, self._Width, self._Height)
        self._Canvas = None
        self._Parent = None

    def get_canvas(self):
        return self._Canvas

    def set_position(self, x, y):
        self._PosX = x
        self._PosY = y
        self._Rect.x = x
        self._Rect.y = y


    def set_size(self, width, height):
        self._Height = height
        self._Width = width
        self._Rect.height = height
        self._Rect.width = width

    def set_color(self, color):
        self._Color = color

    def set_bgcolor(self, color):
        self._BG_Color = color

    def set_parent(self, parent):
        self._Parent = parent

    def get_rect(self):
        return self._Rect

    def Draw(self):
        if self._BG_Color is not None and self.parent is not None:
            pygame.draw.rect(self._Parent.get_canvas(), self._BG_Color, self._Rect)

    def handle_event(self, evt):
        pass