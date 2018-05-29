# -*- coding: utf-8 -*- 

import myvars
from brightness_page import BrightnessPage


def InitBrightnessPage(main_screen):
    myvars.BrightnessPage = BrightnessPage()

    myvars.BrightnessPage._Screen = main_screen
    myvars.BrightnessPage._Name = "Brightness"
    myvars.BrightnessPage.Init()
