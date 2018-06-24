#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import sys

import pygame

if not pygame.display.get_init():
    pygame.display.init()
if not pygame.font.get_init():
    pygame.font.init()

# from wicd import misc
import config_manager as config
import plugins
import skin_manager as SkinManager

import GdUI as UI

plugins = plugins.LoadPlugins(config)
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
    global sound_patch

    screen = UI.Screen(fps=30, bg_color=SkinManager.get_color("background"))

    cont = UI.Container(10, 10, 50, 50, bg_color=(192, 192, 192))

    lbl = UI.Label(0, 0, auto_resize=True)
    lbl.set_text("Hello the World")
    lbl.set_bgcolor(None)
    lbl.set_color(SkinManager.get_color("URL"))
    lbl.set_font("noto_40")

    img = UI.Image(x=30, y=30, image=UI.ImageManager.get_image("blank_icon"))

    corner_ul = UI.Image(x=0, y=0, image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 1))
    corner_ur = UI.Image(x=screen.get_rect().width - 10, y=0,
                         image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 2))
    corner_dl = UI.Image(x=0, y=screen.get_rect().height - 10,
                         image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 3))
    corner_dr = UI.Image(x=screen.get_rect().width - 10, y=screen.get_rect().height - 10,
                         image=UI.ImageManager.get_sprite("corners_tiles", 10, 10, 4))

    cont.add_child(lbl)

    bottom_bar = UI.FlowContainer(x=0, y=screen.get_rect().height - 20, width=screen.get_rect().width, height=20,
                                  bg_color=(83, 83, 83))

    lblA = UI.Label(0, 0, auto_resize=True)
    lblA.set_text("A")
    lblA.set_color(SkinManager.get_color("URL"))
    lblA.set_font("noto_13")

    lblB = UI.Label(0, 0, auto_resize=True)
    lblB.set_text("D")
    lblB.set_color(SkinManager.get_color("URL"))
    lblB.set_font("noto_13")

    lblC = UI.Label(0, 0, auto_resize=True)
    lblC.set_text("C")
    lblC.set_color((0, 255, 0))
    lblC.set_font("noto_13")

    lblD = UI.Label(0, 0, auto_resize=True)
    lblD.set_text("C")
    lblD.set_color((255, 0, 0))
    lblD.set_font("noto_13")

    bottom_bar.add_left_child(lblA)
    bottom_bar.add_left_child(lblB)

    bottom_bar.add_right_child(lblC)
    bottom_bar.add_right_child(lblD)

    bottom_bar.set_margin(10)

    screen.add_child(img)
    screen.add_child(cont)

    screen.add_child(bottom_bar)

    screen.add_child(corner_ul)
    screen.add_child(corner_ur)
    screen.add_child(corner_dl)
    screen.add_child(corner_dr)

    x = 0
    y = 10
    while True:
        for event in pygame.event.get():
            process_event(event, screen)

        screen.Draw()

        cont.set_position(x, y)
        x += 5
        if x > 320:
            x = 0
        y += 1
        while(y > 240):
            y = y * 2 / 240


    # socket_thread(main_screen)


def init():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    if pygame.image.get_extended() == False:
        print("This pygame does not support PNG")
        sys.exit()


    main_loop()


init()
