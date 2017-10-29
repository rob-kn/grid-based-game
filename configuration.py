# Will hold all global variables and will be imported first into the main program.
# Also initialises pygame to create other constants.

import pygame as pg

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
GRID_SQUARE_SIZE = 50
GRID_HEIGHT = int((WINDOW_HEIGHT / GRID_SQUARE_SIZE) - 1)
GRID_WIDTH = int((WINDOW_WIDTH / GRID_SQUARE_SIZE) - 1)
GRID_DESIGN = ["##########",
               "#        #",
               "# #    # #",
               "#        #",
               "#        #",
               "#        #",
               "#        #",
               "# #    # #",
               "#        #",
               "##########"]
SCORE = 0
done = False
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pg.init()
screen = pg.display.set_mode(WINDOW_SIZE)
clock = pg.time.Clock()
FONT = pg.font.Font('amatic/Amatic-Bold.ttf', 32)
