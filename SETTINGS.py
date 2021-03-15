#SETTINGS
#game
curl = 0
fps = 31
caption = "Meta beta 3B.1"
mode = 1
vol = 1
mvol = 1
mshowing = True
cl_size = None
chl = False
quit_game = False
game_won = False
dt = 0
cfps = 0
stat = {}
playsecs = 0
#lvl
gl_size = 4
gl_am = 100
lvl_list = []
seg_list = []
clvl_list = []
glvl_list = []
tlvl_list = []
seed = None
play_cus = False
play_new = False
play_tutor = False
#canvas
ctw = 700
cth = 550 #600
caw = 0
cmw, cmh = None, None
wh = int(cth + (cth * 0.15))
sw_mode = False
axes = (0, 0)
scr_shk = 0
#raycast
rsl = 140
fov = 60
render = 10
shade = False
shade_rgba = (0,0,0,255)
shade_visibily = 1000
zbuffer = []
mid_sl_l = None
mid_sl = None
mid_ray_pos = None
raylines = []
#tile
tl_size = 64
all_tl = []
trg_tl = []
rendered_tl = []
wlk_area = []
all_doors = []
end_ang = 0
#player
plr_spd = 270
sens = 0.25
plr_ang = 270
og_plr_hlt = 25
og_plr_arm = 5
(plr_hlt,
 plr_arm,
 plr_pos,
 plr_map_pos,
 plr_rect) = (
 og_plr_hlt,
 og_plr_arm,
 [0,0],
 [],
 None)
mbtn_active = False
m2btn_active = False
rld_key_active = False
aim = False
player_states = {
    'dead' : False,
    'hurt' : False,
    'heal' : False,
    'armor' : False,
    'invopen' : False,
    'fade' : False,
    'black' : False,
    'title' : False,
    'cspeed' : 0,
    }
plr = None
last_plr_map_pos = None
#texture
txr_darken = 100
txr_list = []
#weapon
unlim_ammo = False
cur_gun = None
next_gun = None
prev_gun = None
gun_list = []
grnd_wpn = None
#NPC
ignr_plr = False
npc_list = []
npc_types = []
npc_sndpks = []
#inventory
held_ammo = {}
max_ammo = {}
inventory = {
    'primary': None,
    'secondary': None,
    'melee': None}
item_types = []
inv_strings_updated = False
#tile conf
tile_texture = {}
tile_solid = {
    0 : False,
    1 : True,
    2 : True,
    3 : True,
    4 : True,
    5 : True,
    6 : True,
    7 : True,
    8 : True,
    9 : True,
    10 : False,
    
    11 : True,
    12 : True,
    13 : True,
    14 : True,
    15 : True,
    16 : True,
    17 : True,
    18 : True,
    
    19 : True,
    20 : True,
    21 : True,
    22 : True,
    23 : True,
    24 : True,
    25 : True,
    }
tile_visible = { #Sprite tiles are not visible
    0 : False,
    1 : True,
    2 : True,
    3 : True,
    4 : True,
    5 : True,
    6 : True,
    7 : True,
    8 : False,
    9 : False,
    10 : False,
    
    11 : True,
    12 : True,
    13 : True,
    14 : True,
    15 : True,
    16 : False,
    17 : False,
    18 : False,
    
    19 : True,
    20 : True,
    21 : True,
    22 : True,
    23 : True,
    24 : True,
    25 : False,
    }
texture_type = { #air, wall, trigger, sprite
    0 : 'air',
    1 : 'wall',
    2 : 'wall',
    3 : 'wall',
    4 : 'wall',
    5 : 'end',
    6 : 'vdoor',
    7 : 'hdoor',
    8 : 'sprite',
    9 : 'sprite',
    10 : 'sprite',
    
    11 : 'wall',
    12 : 'wall',
    13 : 'wall',
    14 : 'wall',
    15 : 'end',
    16 : 'sprite',
    17 : 'sprite',
    18 : 'sprite',
    
    19 : 'wall',
    20 : 'wall',
    21 : 'wall',
    22 : 'end',
    23 : 'vdoor',
    24 : 'hdoor',
    25 : 'sprite',
    }
#sprite
all_spr = []
#item
all_items = []
#colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (140, 50, 20)
DARKGRAY = (50, 50, 50)
DARKRED = (80, 0, 0)
DARKGREEN = (0, 100, 0)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 225)
LIGHTGRAY = (150, 150, 150)
LIGHTGREEN = (100, 255, 100)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
#Create a new tile / sprite tile:
#1. Create texture and add it to TEXTURES.py in the marked area for tiles.
#2. Give the tile by ID the settings you want in dictionaries above.
#3. Make sure that all tiles has a texture or sprite. Invisible tiles can use null.png
#4. Note that Sprite tiles are not visible. The tile itself is not rendered.
#Note: A tile can be solid, but invisible, but not vice versa

#Create a new sprite (NPC):
#1. Create the texture and add it to TEXTURES.py in the marked area for NPC's
#2. Assign the sprite an ID and make sure the sprite is added to SETTINGS.all_sprites.
#3. Add the sprite (ID) to the texture_type dictionary above. Call it 'sprite'.
#4. Fill out the arguments to make a sprite (pos, path)

#ctrl
temp = []
