# -*- coding: utf-8 -*- 

import myvars
from sound_page import SoundPage


def InitSoundPage(main_screen):
    myvars.SoundPage = SoundPage()

    myvars.SoundPage._Screen = main_screen
    myvars.SoundPage._Name = "Sound volume"
    myvars.SoundPage.Init()
