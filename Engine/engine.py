#!/usr/bin/python3
import pygame as pg
from pygame.locals import *
import os
import sys

colors= {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        }

class Engine:
    def __init__(self, w, h, bg_layer, bg_layer2, world):
        self.w= w
        self.h= h
        self.bg= bg_layer,
        self.bg2= bg_layer2
        self.world= world
        pg.init()
        self.win= pg.display.set_mode((self.w, self.h))
        pg.display.set_caption('')
    def mv_viewport(self, x, y):
        for e in self.bg:
            for e2 in e:
                e.x, e.y= x+ e.x, y+ e.y
        for e in self.world:
            e.x, e.y= x+e.x, y+ e.y
    def render(self):
        #TODO: add draw bg and terrain functionality
        pg.display.update()
