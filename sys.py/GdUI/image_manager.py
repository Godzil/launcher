import pygame

if not pygame.font.get_init():
    pygame.font.init()

__images = {}


def add_image(name: str, imagefile: str):
    surf = pygame.image.load(imagefile)
    __images[name] = surf


def get_image(name: str):
    try:
        return __images[name]
    except KeyError:
        print("WARN: ImageManager': Image '{name}' is not defined".format(name=name))
        return None


def get_sprite(name: str, width: int, height: int, pos: int):
    try:
        img = __images[name]
    except KeyError:
        print("WARN: ImageManager': Image '{name}' is not defined".format(name=name))
        return None

    x_count = img.get_width() // width
    pos_x = pos % x_count
    pos_y = (pos // x_count) - 1

    return img.subsurface((pos_x * width, pos_y * height, width, height))


def del_image(name: str):
    try:
        __images[name] = None
    except KeyError:
        print("WARN: ImageManager': Trying to remove image '{name}' which was not defined".format(name=name))