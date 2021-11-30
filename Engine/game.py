#!/usr/bin/python3
from engine import *
from player import Player
import json

#returns path of this directory
dirname= os.path.join(os.path.dirname(__file__), '..')

class Game_status:
    def __init__(self, argv):
        file_name= argv
        with open(os.path.join(dirname, file_name), 'r') as f:
            self.game_status= json.load(f)
        # self.game_status['bg']= self.game_status['bg'].format(dirname)

class Game:
    def __init__(self, game_status, keymaps_file, settings_file):
        with open(os.path.join(dirname, 'Settings', keymaps_file), 'r') as f:
            self.keymaps= json.load(f)
        with open(os.path.join(dirname, 'Settings', settings_file), 'r') as f:
            self.settings= json.load(f)

        self.convertKeymaps()

        terrain= game_status.game_status['world']
        #contains world content
        world= []
        bg= game_status.game_status['bg']
        w, h= self.settings['w'], self.settings['h']
        #TODO: use inventory
        #TODO: move inventory into player class/object
        inventory= game_status.game_status['inventory']

        #creates game objects for example player and adds world content
        for i in range(len(terrain)):
            world.append(
                globals()[terrain[i]['class_name']](
                    terrain[i]['pos'],
                    terrain[i]['object_parameters']['texture'],
                    terrain[i]['object_parameters']['scale'],
                    )
                )
        bg_formatted= []
        #loads background images
        for i in bg:
            print(dirname+ i['img'])
            img= pg.image.load(dirname+ i['img'])
            img= pg.transform.scale( img, (img.get_width()* i['scale'], img.get_height()* i['scale']) )
            bg_formatted.append({
                'img': img,
                'pos': Vector2(i['pos']['x'], i['pos']['y'])
            })
        
        #creates engine object
        self.engine= Engine(
                w,
                h,
                title= '',
                bg= bg_formatted, 
                world= world,
                )

        #creates pygame clock object
        self.clock= pg.time.Clock()

    def convertKeymaps(self):
        for k in self.keymaps:
            self.keymaps[k]= pg.key.key_code(self.keymaps[k])
    #game loop
    def loop(self):
        while True:
            #renders content
            self.engine.render()

            #handles close window event
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    sys.exit()
                if event.type== pg.KEYDOWN:
                    if event.key== self.keymaps['forward']:
                        print('forward')

            #enforcing fps
            self.clock.tick(60)

if __name__== '__main__':
    game_status= globals()['Game_status'](os.path.join(dirname, 'SampleMap', 'map.json'))
    game= Game(game_status, 'keymaps.json', 'settings.json')
    game.loop()
