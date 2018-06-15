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
import config
import plugins
import skin_manager as SkinManager

import GdUI as UI

plugins = plugins.LoadPlugins(config)
fonts = UI.FontManager
myscriptname = os.path.basename(os.path.realpath(__file__))


def process_event(event, ui_root: UI.Widget):
    if event is not None:

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        else:
            ui_root.handle_event(event)

def socket_thread(main_screen):
    socket_path = "/tmp/gameshell"
    if os.path.exists(socket_path):
        os.remove(socket_path)

    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(socket_path)
    while True:
        server.listen(1)
        conn, addr = server.accept()
        datagram = conn.recv(1024)
        if datagram:
            tokens = datagram.strip().split()

            if tokens[0].lower() == "esc":
                escevent = pygame.event.Event(pygame.KEYDOWN, {'scancode': 9, 'key': 27, 'unicode': u'\x1b', 'mod': 0})
                current_page_key_down_cb = getattr(main_screen._CurrentPage, "KeyDown", None)

                if current_page_key_down_cb is not None:
                    if callable(current_page_key_down_cb):
                        main_screen._CurrentPage.KeyDown(escevent)

            if tokens[0].lower() == "quit":
                conn.close()
                on_exit_cb = getattr(main_screen, "OnExitCb", None)
                if on_exit_cb is not None:
                    if callable(on_exit_cb):
                        main_screen.OnExitCb(None)

                exit()

            if tokens[0].lower() == "poweroff":
                escevent = pygame.event.Event(pygame.KEYDOWN, {'scancode': 9, 'key': 27, 'unicode': u'\x1b', 'mod': 0})
                for i in range(0, 5):
                    current_page_key_down_cb = getattr(main_screen._CurrentPage, "KeyDown", None)

                    if current_page_key_down_cb is not None:
                        if callable(current_page_key_down_cb):
                            main_screen._CurrentPage.KeyDown(escevent)

                    if main_screen._MyPageStack.Length() == 0:  ## on Top Level
                        break

                if main_screen._CurrentPage._Name == "GameShell":
                    for i in main_screen._CurrentPage._Icons:
                        if i._MyType == ICON_TYPES["FUNC"]:
                            if i._Label.GetText() == "PowerOFF":
                                api_cb = getattr(i._CmdPath, "API", None)

                                if api_cb is not None:
                                    if callable(api_cb):
                                        i._CmdPath.API(main_screen)


def main_loop():
    global sound_patch

    screen = UI.Screen(fps=30, bg_color=SkinManager.get_color("background"))

    cont = UI.Container(10, 10, 50, 50, bg_color=(192, 192, 192))

    lbl = UI.Label(0, 0, auto_resize=True)
    lbl.SetText("Hello the World")
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

    screen.add_child(img)
    screen.add_child(cont)

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
