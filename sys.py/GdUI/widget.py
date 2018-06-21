import pygame

class Widget:
    borderTop = 1
    borderBottom = 2
    borderLeft = 4
    borderRight = 8

    def __init__(self, x=0, y=0, width=7, height=7, color=None, bg_color=None, border=0, border_color=None):
        self._PosX = x
        self._PosY = y
        self._Width = width
        self._Height = height

        self._Color = color
        self._BG_Color = bg_color
        self._BorderColor = border_color
        self._Rect = pygame.Rect(self._PosX, self._PosY, self._Width, self._Height)
        self._Canvas = None
        self._Parent = None
        self._Border = border

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

    def set_border(self, border, color):
        self._Border = border
        self._BorderColor = color

    def Draw(self):
        if self._BG_Color is not None and self._Parent is not None:
            pygame.draw.rect(self._Parent.get_canvas(), self._BG_Color, self._Rect)

    def _DrawBorder(self):
        if self._Border > 0:
            if self._Border & self.borderTop:
                pygame.draw.line(self._Parent.get_canvas(), self._BG_Color,
                                 (self._PosX, self._PosY), (self._PosX + self._Width, self._PosY), 1)

            if self._Border & self.borderLeft:
                pygame.draw.line(self._Parent.get_canvas(), self._BG_Color,
                                 (self._PosX, self._PosY), (self._PosX, self._PosY + self._Height), 1)

            if self._Border & self.borderBottom:
                pygame.draw.line(self._Parent.get_canvas(), self._BG_Color,
                                 (self._PosX, self._PosY + self._Height),
                                 (self._PosX + self._Width, self._PosY + self._Height), 1)

            if self._Border & self.borderRight:
                pygame.draw.line(self._Parent.get_canvas(), self._BG_Color,
                                 (self._PosX + self._Width, self._PosY),
                                 (self._PosX + self._Width, self._PosY + self._Height), +1)

    def handle_event(self, evt):
        pass

    def reload(self):
        pass