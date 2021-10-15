#!/usr/bin/python3
from engine import *

engine= Engine(500, 500, [ ['grass', 500, 500, ['img', os.path.join(os.path.expanduser('~'), 'Py', 'konkurs', 'Assets', 'Images', 'grass.png')]] ], [], [])
clock= pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    engine.render()
    clock.tick(60)
