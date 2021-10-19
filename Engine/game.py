#!/usr/bin/python3
from engine import *
import json

#returns path of this directory
dirname= os.path.join(os.path.dirname(__file__), '..')

class Game_status:
    def __init__(self, argv):
        file_name= argv
        with open(os.path.join(dirname, file_name), 'r') as f:
            self.game_status= json.loads(f)

class Game:
    def __init__(self, game_status, keymaps_file, settings_file):
        with open(os.path.join(dirname, 'Settings', keymaps_file), 'r') as f:
            self.keymaps= json.loads(f)
        with open(os.path.join(dirname, 'Settings', settings_file), 'r') as f:
            self.settings= json.loads(f)

        #contains world content
        world= game_status.game_status['world']
        bg= game_status.game_status['bg']
        w, h= self.settings['w'], self.settings['h']

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

# world= [
        # {
        #     'pos': Vector2(20, 20),
        #     'img': os.path.join(dirname, 'Assets', 'Images', 'sample.png')
        #     }
        # ]



if __name__ is '__main__':
    game_status= Game_status(os.path.join('SampleMap', 'map.json'))
    game= Game(game_status, 'keymaps.json', 'settings.json')
    game.loop()
