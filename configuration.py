import pygame as pg

GRID_SQUARE_SIZE = 64

# LEFT_PANEL_WIDTH = 100
# RIGHT_PANEL_WIDTH = 100

LEFT_PANE_WIDTH = 200
LEFT_PANE_STARTX = 0
LEFT_PANE_STARTY = 0

CAMERA_STARTX = LEFT_PANE_WIDTH
CAMERA_STARTY = 0
CAMERA_HEIGHT = 11
CAMERA_WIDTH = 13
CAMERA_HEIGHT_PIXELS = CAMERA_HEIGHT * GRID_SQUARE_SIZE
CAMERA_WIDTH_PIXELS = CAMERA_WIDTH * GRID_SQUARE_SIZE

RIGHT_PANE_WIDTH = 200
RIGHT_PANE_STARTX = LEFT_PANE_WIDTH + CAMERA_WIDTH_PIXELS
RIGHT_PANE_STARTY = 0

SCREEN_HEIGHT = CAMERA_HEIGHT_PIXELS
SCREEN_WIDTH = LEFT_PANE_WIDTH + CAMERA_WIDTH_PIXELS + RIGHT_PANE_WIDTH
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
COMPLETE_GRID = [line.strip() for line in open('maps/level_0_map.txt').readlines()]

SCORE = 0
done = False
FPS = 60

# Colors
WHITE = (255, 255, 255)
SILVER = (192, 192, 192)
GREY = (64, 64, 64)
SLATE_GREY = (112, 128, 144)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

# Fonts
FONT_48 = pg.font.Font('amatic/Amatic-Bold.ttf', 48)
FONT_32 = pg.font.Font('amatic/Amatic-Bold.ttf', 32)
FONT_32_BOLD = pg.font.Font("amatic/Amatic-Bold.ttf", 32)
FONT_16 = pg.font.Font('amatic/Amatic-Bold.ttf', 16)
NAMES_FONT = pg.font.Font(None, 16)

# Graphics
# Map
wall_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-dngn/wall/brick_dark0.png")
wall_img = pg.transform.scale(wall_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
floor_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-dngn/floor/tomb0.png")
floor_img = pg.transform.scale(floor_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))

# Player
# player_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/player/base/human_m.png")
# player_img = pg.transform.scale(player_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
# player_legs = pg.image.load("graphics/crawl-tiles Oct-5-2010/player/legs/leg_armor01.png")
# player_legs = pg.transform.scale(player_legs, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
# player_body = pg.image.load("graphics/crawl-tiles Oct-5-2010/player/body/chainmail3.png")
# player_body = pg.transform.scale(player_body, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
#
# deep_troll = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-mon/deep_troll.png")
# deep_troll = pg.transform.scale(deep_troll, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))

# Enemies
# giant_eye_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-mon/giant_eyeball.png")
# giant_eye_img = pg.transform.scale(giant_eye_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
# grey_rat_img = pg.image.load("graphics/crawl-tiles Oct-5-2010/dc-mon/animals/grey_rat.png")
# grey_rat_img = pg.transform.scale(grey_rat_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))

# Items
# health_potion = pg.image.load("graphics/crawl-tiles Oct-5-2010/item/potion/ruby.png")
# health_potion = pg.transform.scale(health_potion, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
