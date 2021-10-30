import pygame as pg
import os
import sys
import numpy as np
from pygame.math import Vector2
from math import *

#colors that can be used anywhere in this project
colors= {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        }

class Engine:
    def __init__(self, w, h, title, bg_img, world):
        self.w= w
        self.h= h
        self.bg_img= pg.image.load(bg_img)
        self.world= world

        #initializes pygame
        pg.init()
        #creates pygame window
        self.win= pg.display.set_mode((self.w, self.h))
        pg.display.set_caption(title)
    #moves viewport by moving it's content
    def mv_viewport(self, x, y):
        #TODO: modify and finish this
        for e in self.world:
            e.x, e.y= x+e.x, y+ e.y
    def drawBgImage(self):
        #TODO: modify and finish this
        for x in np.arange(0, self.w+ self.bg_img.get_width(), self.bg_img.get_width()):
            for y in np.arange(0, self.h+ self.bg_img.get_height(), self.bg_img.get_height()):
                self.win.blit(self.bg_img, (x, y))
    #draws content from list
    def draw(self, elements):
        for e in elements:
            self.win.blit(e.getImg(), e.getPos())
    #renders content
    def render(self):
        self.drawBgImage()
        #draws world
        self.draw(self.world)

        #updates window content
        pg.display.update()
