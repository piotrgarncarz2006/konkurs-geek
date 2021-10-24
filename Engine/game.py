#!/usr/bin/python3
from engine import *
import json

#returns path of this directory
dirname= os.path.join(os.path.dirname(__file__), '..')

class Game_status:
    def __init__(self, argv):
        file_name= argv
        with open(os.path.join(dirname, file_name), 'r') as f:
            self.game_status= json.load(f)
        self.game_status['bg']= self.game_status['bg'].format(dirname)

class Game:
    def __init__(self, game_status, keymaps_file, settings_file):
        with open(os.path.join(dirname, 'Settings', keymaps_file), 'r') as f:
            self.keymaps= json.load(f)
        with open(os.path.join(dirname, 'Settings', settings_file), 'r') as f:
            self.settings= json.load(f)

        #contains world content
        world= game_status.game_status['world']
        bg= game_status.game_status['bg']
        w, h= self.settings['w'], self.settings['h']
        #TODO: use inventory
        inventory= game_status.game_status['inventory']

        #creates engine object
        self.engine= Engine(w, h, title= '', bg_img= os.path.join(dirname, 'Assets', 'Images', 'grass.png'), world= world)

        #creates pygame clock object
        self.clock= pg.time.Clock()
    #game loop
    def loop(self):
        while True:
            #handles close window event
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            #renders content
            self.engine.render()
            #enforcing fps
            self.clock.tick(60)

if __name__== '__main__':
    game_status= globals()['Game_status'](os.path.join(dirname, 'SampleMap', 'map.json'))
    game= Game(game_status, 'keymaps.json', 'settings.json')
    game.loop()
