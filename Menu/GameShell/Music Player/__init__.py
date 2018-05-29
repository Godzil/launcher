# -*- coding: utf-8 -*-


from . import myvars
## local UI import
from . import pages

def Init(main_screen):
    pages.InitPoller()

    pages.InitListPage(main_screen)
    pages.InitMusicLibPage(main_screen)
    pages.InitSpectrumPage(main_screen)


def API(main_screen):
    if main_screen != None:
        main_screen.PushCurPage()
        main_screen.SetCurPage(myvars.PlayListPage)
        main_screen.Draw()
        main_screen.SwapAndShow()
