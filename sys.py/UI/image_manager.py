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

    surf = pygame.Surface((width, height))
    x_count = img.get_width() // width
    y_count = img.get_height() // height

    pos_x = pos % x_count
    pos_y = pos // y_count
    # TODO: Need to make sure the surface is fully transparent, or that we blindly copy the pixel data
    surf.blit(img, dest=(0, 0), area=(pos_x * width, pos_y * height, width, height), special_flags=pygame.BLEND_ADD)

    return surf



def del_image(name: str):
    try:
        __images[name] = None
    except KeyError:
        print("WARN: ImageManager': Trying to remove image '{name}' which was not defined".format(name=name))