#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import pygame

if not pygame.display.get_init():
    pygame.display.init()
if not pygame.font.get_init():
    pygame.font.init()

# noinspection PyPep8
import config_manager as config
import plugins
import skin_manager as SkinManager

import GdUI as UI
from interface import main_screen

plugins = plugins.LoadPlugins()
fonts = UI.FontManager
myscriptname = os.path.basename(os.path.realpath(__file__))
SkinManager.load_skin("cpi_default")


def process_event(event, ui_root: UI.Widget):
    if event is not None:

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        else:
            ui_root.handle_event(event)


def main_loop():
    screen_width = config.get("screen_width")
    screen_height = config.get("screen_height")

    screen = UI.Screen(fps=30, width=screen_width, height=screen_height)
    main = main_screen.MainScreen(screen_width, screen_height)

    screen.add_child(main)

    while True:
        for event in pygame.event.get():
            process_event(event, screen)

        screen.Draw()


def init():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    if not pygame.image.get_extended():
        print("This pygame does not support PNG")
        sys.exit()

    main_loop()


init()
