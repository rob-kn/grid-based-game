import pygame as pg
import json

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
MAP_0 = [line.split('\t') for line in open('maps/map_0.csv').readlines()]

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

with open('tile_codes.json') as tc_json_data:
    tile_codes = json.load(tc_json_data)
tile_code_images = {}
for tile_code, fp in tile_codes.items():
    tile_img = pg.image.load(fp)
    tile_img = pg.transform.scale(tile_img, (GRID_SQUARE_SIZE, GRID_SQUARE_SIZE))
    tile_code_images[tile_code] = tile_img

