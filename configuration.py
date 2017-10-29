import pygame as pg

GRID_SQUARE_SIZE = 50
CAMERA_HEIGHT = 11
CAMERA_WIDTH = 13
CENTER_X = int(CAMERA_WIDTH / 2 + 1)
CENTER_Y = int(CAMERA_HEIGHT / 2 + 1)
SCREEN_HEIGHT = CAMERA_HEIGHT * GRID_SQUARE_SIZE
SCREEN_WIDTH = CAMERA_WIDTH * GRID_SQUARE_SIZE
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
COMPLETE_GRID = ["############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "##########        ##########",
                 "########## #    # ##########",
                 "##########        ##########",
                 "##########        ##########",
                 "##########        ##########",
                 "##########        ##########",
                 "########## #    # ##########",
                 "##########        ##########",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################",
                 "############################"]
GRID_WIDTH = len(COMPLETE_GRID[0])
GRID_HEIGHT = len(COMPLETE_GRID)

SCORE = 0
done = False
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()
FONT = pg.font.Font('amatic/Amatic-Bold.ttf', 32)
