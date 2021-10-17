#!/usr/bin/python3
from engine import *

#returns path of this directory
dirname= os.path.dirname(__file__)

#contains world content
world= [
        # {
        #     'pos': (20, 20),
        #     'img': os.path.join(dirname, '..', 'Assets', 'Images', 'sample.png')
        #     }
        ]

engine= Engine(w= 1000, h= 800, title= '', bg_img= os.path.join(dirname, '..', 'Assets', 'Images', 'grass.png'), world= world)

#creates pygame clock object
clock= pg.time.Clock()

#game loop
while True:
    #handles close window event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    #renders content
    engine.render()
    #enforcing fps
    clock.tick(60)
