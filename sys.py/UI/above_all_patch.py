# -*- coding: utf-8 -*- 

import alsaaudio
import pygame
from libs.roundrects import aa_round_rect

## local package import
from .constants import Width, Height
from .fonts import fonts
from .util_funcs import midRect


class AboveAllPatch(object):
    _PosX = Width / 2
    _PosY = Height / 2
    _Width = 50
    _Height = 120

    _Text = ""
    _FontObj = fonts["veramono20"]
    _Parent = None
    _Color = pygame.Color(83, 83, 83)
    _ValColor = pygame.Color(0, 0, 255)
    _CanvasHWND = None
    _TextSurf = None
    _Icons = {}
    _Value = 0

    def __init__(self):
        self._Icons = {}

    def Init(self):
        pass

    def SetCanvasHWND(self, _canvashwnd):
        self._CanvasHWND = _canvashwnd

    def Draw(self):
        start_rect = midRect(self._PosX, self._PosY, self._Width, self._Height, Width, Height)
        aa_round_rect(self._CanvasHWND, start_rect, self._Color, 3, 0, self._Color)

        if self._Value > 10:
            vol_height = int(self._Height * (float(self._Value) / 100.0))
            dheight = self._Height - vol_height

            vol_rect = pygame.Rect(self._PosX - self._Width / 2, self._PosY - self._Height / 2 + dheight, self._Width,
                                   vol_height)

            aa_round_rect(self._CanvasHWND, vol_rect, self._ValColor, 3, 0, self._ValColor)

        else:
            vol_height = 10
            dheight = self._Height - vol_height
            vol_rect = pygame.Rect(self._PosX - self._Width / 2, self._PosY - self._Height / 2 + dheight, self._Width,
                                   vol_height)

            aa_round_rect(self._CanvasHWND, vol_rect, self._ValColor, 3, 0, self._ValColor)


class SoundPatch(AboveAllPatch):
    snd_segs = [[0, 20], [21, 40], [41, 50], [51, 60], [61, 70], [71, 85], [86, 90], [91, 95], [96, 100]]
    _Needle = 0
    
    def Init(self):
        self.SetCanvasHWND(self._Parent._CanvasHWND)

    def VolumeUp(self):
        m = alsaaudio.Mixer()
        vol = m.getvolume()[0]

 #       print("VolumeUp vol %d " % vol)
        for i,v in enumerate(self.snd_segs):
            if  vol >= v[0] and vol <= v[1]:
                self._Needle = i
                break
          
        self._Needle += 1

        if self._Needle > len(self.snd_segs) -1:
            self._Needle = len(self.snd_segs) -1

#        print("Set volume %d" % self.snd_segs[self._Needle][1] )
        m.setvolume( self.snd_segs[self._Needle][0] +  (self.snd_segs[self._Needle][1] - self.snd_segs[self._Needle][0])/2   ) ## prefer bigger one  

        self._Value = self.snd_segs[self._Needle][1]

#        print( self._Value)
        return self._Value

    def VolumeDown(self):
        m = alsaaudio.Mixer()
        vol = m.getvolume()[0]

        for i,v in enumerate(self.snd_segs):
            if  vol >= v[0] and vol <= v[1]:
                self._Needle = i
                break

        self._Needle -= 1
        if self._Needle < 0:
            self._Needle = 0
        
        vol =  self.snd_segs[self._Needle][0] ## prefer smaller one
        
        if vol < 0:
            vol = 0
        m.setvolume(vol)

#        print(vol)

        self._Value = vol
        return vol

    def Draw(self):
        # 200 total width
        # h = 40
        for i in range(0,self._Needle+1):
            # w = 10,h = 40
            vol_rect = pygame.Rect(80 + i * 20, self._Height / 2 + 20, 10, 40)

            aa_round_rect(self._CanvasHWND,vol_rect, self._Parent._SkinManager.GiveColor("Front"),3,0, self._Parent._SkinManager.GiveColor("Front"))
