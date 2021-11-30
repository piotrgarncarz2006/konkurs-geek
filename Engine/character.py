import os
import pygame as pg
from pygame.math import Vector2

#returns path of this directory
dirname= os.path.join(os.path.dirname(__file__), '..')

def formatImage(image_path):
    image_path= image_path.format(dirname)

class Character:
    def __init__(self, pos, texture, scale, inventory):
        print('character init')
        #TODO: finish this

        self.scale= scale
        self.pos= Vector2(pos['x'], pos['y'])
        self.texture= texture
        self.loadImages(self.texture)
        self.img= self.texture['front'][0]
        self.inventory= inventory

    def getImg(self):
        return self.img
    def getPos(self):
        return self.pos
    def formatImage(self):
        self.img= formatImage(self.img)
    def loadImages(self, texture):
        print(texture)
        for k, e in texture.items():
            print(e)
            for i in range(len(e)):
                e[i]= dirname+ e[i]
                e[i]= pg.image.load(e[i])
                e[i]= pg.transform.scale(e[i], (e[i].get_width()* self.scale, e[i].get_height()* self.scale) )
            print(e)
            print('------')
