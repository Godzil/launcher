# -*- coding: utf-8 -*- 

from . import list_page

from . import myvars


def InitListPage(main_screen):
    myvars.ListPage = list_page.ListPage()

    myvars.ListPage._Screen = main_screen
    myvars.ListPage._Name = "Setting List"
    myvars.ListPage.Init()
