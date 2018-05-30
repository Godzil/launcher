#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import sys

import pygame

# from wicd import misc
import config
import plugins
from UI.above_all_patch import SoundPatch
# local UI import
from UI.constants import Width, Height, bg_color, DT, GMEVT, RUNEVT, RUNSYS, ICON_TYPES
from UI.foot_bar import FootBar
from UI.icon_pool import MyIconPool
from UI.main_screen import MainScreen
from UI.title_bar import TitleBar
from UI.util_funcs import GetExePath, X_center_mouse

if not pygame.display.get_init():
    pygame.display.init()
if not pygame.font.get_init():
    pygame.font.init()

conf = config.Config()
plugins = plugins.LoadPlugins(conf)

sound_patch = None

myscriptname = os.path.basename(os.path.realpath(__file__))

def process_event(event, main_screen):
    global sound_patch
    if event is not None:
        pygame.event.clear()

        if event.type == pygame.ACTIVEEVENT:
            print(" ACTIVE EVENT !")

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == GMEVT:
            main_screen.Draw()
            main_screen.SwapAndShow()
            pygame.event.clear(GMEVT)

        if event.type == RUNEVT:

            if conf.get("DontLeave") is True:
                os.chdir(GetExePath())
                os.system("/bin/sh -c " + event.message)
            else:
                on_exit_cb = getattr(main_screen, "OnExitCb", None)
                if on_exit_cb is not None:
                    if callable(on_exit_cb):
                        main_screen.OnExitCb(event)

                pygame.quit()
                os.chdir(GetExePath())
                exec_app_cmd = event.message
                exec_app_cmd += "; sync & cd " + GetExePath() + "; exec python " + myscriptname
                print(exec_app_cmd)
                os.execlp("/bin/sh", "/bin/sh", "-c", exec_app_cmd)
                os.chdir(GetExePath())
                os.exelp("python", "python", " " + myscriptname)
                sys.exit(-1)

        if event.type == RUNSYS:
            if conf.get("DontLeave") is True:
                os.chdir(GetExePath())
                os.system("/bin/sh -c " + event.message)
            else:
                pygame.quit()
                os.chdir(GetExePath())
                exec_app_cmd = event.message
                exec_app_cmd += "; sync & cd " + GetExePath() + "; exec python " + myscriptname
                print(exec_app_cmd)
                os.execlp("/bin/sh", "/bin/sh", "-c", exec_app_cmd)
                os.chdir(GetExePath())
                os.exelp("python", "python", " " + myscriptname)

        # if event.type == pygame.KEYUP:
        #    pygame.event.clear(pygame.KEYDOWN)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                on_exit_cb = getattr(main_screen, "OnExitCb", None)

                if on_exit_cb is not None:
                    if callable(on_exit_cb):
                        main_screen.OnExitCb(event)

                sys.exit()

            ###########################################################
            # if event.key == pygame.K_ESCAPE:
            #    pygame.event.clear()

            key_down_cb = getattr(main_screen, "KeyDown", None)
            if key_down_cb is not None:
                if callable(key_down_cb):
                    main_screen.KeyDown(event)

# @misc.threaded
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
                if current_page_key_down_cb != None:
                    if callable(current_page_key_down_cb):
                        main_screen._CurrentPage.KeyDown(escevent)

            if tokens[0].lower() == "quit":
                conn.close()
                on_exit_cb = getattr(main_screen, "OnExitCb", None)
                if on_exit_cb != None:
                    if callable(on_exit_cb):
                        main_screen.OnExitCb(None)

                gobject_main_loop.quit()
                exit()

            if tokens[0].lower() == "poweroff":
                escevent = pygame.event.Event(pygame.KEYDOWN, {'scancode': 9, 'key': 27, 'unicode': u'\x1b', 'mod': 0})
                for i in range(0, 5):
                    current_page_key_down_cb = getattr(main_screen._CurrentPage, "KeyDown", None)
                    if current_page_key_down_cb != None:
                        if callable(current_page_key_down_cb):
                            main_screen._CurrentPage.KeyDown(escevent)

                    if main_screen._MyPageStack.Length() == 0:  ## on Top Level
                        break

                if main_screen._CurrentPage._Name == "GameShell":
                    for i in main_screen._CurrentPage._Icons:
                        if i._MyType == ICON_TYPES["FUNC"]:
                            if i._Label.GetText() == "PowerOFF":
                                api_cb = getattr(i._CmdPath, "API", None)
                                if api_cb != None:
                                    if callable(api_cb):
                                        i._CmdPath.API(main_screen)


def main_loop():
    global sound_patch

    title_bar = TitleBar()
    title_bar.Init(screen)
    foot_bar = FootBar()
    foot_bar.Init(screen)

    main_screen = MainScreen()
    main_screen._HWND = screen
    main_screen._TitleBar = title_bar
    main_screen._FootBar = foot_bar
    main_screen.Init()
    main_screen.ReadTheDirIntoPages("../Menu", 0, None)
    main_screen.FartherPages()

    title_bar._SkinManager = main_screen._SkinManager
    foot_bar._SkinManager  = main_screen._SkinManager
    sound_patch = SoundPatch()
    sound_patch._Parent = main_screen
    sound_patch.Init()

    screen.fill(bg_color)
    main_screen.Draw()
    main_screen.SwapAndShow()

    while True:
        for event in pygame.event.get():
            process_event(event, main_screen)

        pygame.time.Clock().tick(30)
    # socket_thread(main_screen)


def init():
    pass


    os.environ['SDL_VIDEO_CENTERED'] = '1'
    X_center_mouse()

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    SCREEN_SIZE = (Width, Height)
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, GMEVT, RUNEVT, RUNSYS])

    pygame.key.set_repeat(DT + DT * 6 + DT // 2, DT + DT * 3 + DT // 2)

    MyIconPool.Init()

    if pygame.image.get_extended() == False:
        print("This pygame does not support PNG")
        sys.exit()

    main_loop()
