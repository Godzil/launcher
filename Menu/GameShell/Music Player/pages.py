# -*- coding: utf-8 -*- 

# from libs.MPD import poller

from . import myvars
from .mpd_spectrum_page import MPDSpectrumPage
from .music_lib_list_page import MusicLibListPage
from .play_list_page import PlayListPage


def InitPoller():
    myvars.Poller = None
    # try:
    #    myvars.Poller = poller.MPDPoller(host=MPD_socket)
    #    myvars.Poller.connect()
    # except:
    #    myvars.Poller = None


def InitMusicLibPage(main_screen):
    myvars.MusicLibListPage = MusicLibListPage()
    myvars.MusicLibListPage._Screen = main_screen
    myvars.MusicLibListPage._Name = "Music Library"
    myvars.MusicLibListPage.Init()


def InitListPage(main_screen):
    myvars.PlayListPage = PlayListPage()

    myvars.PlayListPage._Screen = main_screen
    myvars.PlayListPage._Name = "Play List"
    myvars.PlayListPage.Init()


def InitSpectrumPage(main_screen):
    myvars.SpectrumPage = MPDSpectrumPage()
    myvars.SpectrumPage._Screen = main_screen
    myvars.SpectrumPage._Name = "Spectrum"
    myvars.SpectrumPage.Init()
