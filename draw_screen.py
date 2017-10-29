# Will consist of drawing the current grid and then drawing the player on that grid.
# This should be future implemented for the player to stay centered (Surrounding grid moved instead).
#
# This is where graphics will be loaded
import configuration as conf
import pygame as pg


def draw_game():
    conf.screen.fill((0, 0, 0))
    for y, row in enumerate(conf.GRID_DESIGN):
        for x, tile in enumerate(row):
            if tile == '#':
                pg.draw.rect(conf.screen, conf.wall_color,
                                 pg.Rect(x * conf.GRID_SQUARE_SIZE, y * conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE,
                                         conf.GRID_SQUARE_SIZE))
            elif tile == ' ':
                pg.draw.rect(conf.screen, conf.empty_color,
                             pg.Rect(x * conf.GRID_SQUARE_SIZE, y * conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE,
                             conf.GRID_SQUARE_SIZE))
            elif tile == 'T':
                pg.draw.rect(conf.screen, conf.target_color,
                                 pg.Rect(x * conf.GRID_SQUARE_SIZE, y * conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE,
                                         conf.GRID_SQUARE_SIZE))
            elif tile == 'P':
                # player should be stored server side so will not be in map variable
                pass
    # this draws the player (moving or not)
    pg.draw.rect(conf.screen, conf.player_color, pg.Rect(conf.pos[0], conf.pos[1], conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE))
    # draw score
    score_text = conf.FONT.render("Score - {0}".format(conf.SCORE), 1, (255, 255, 255))
    conf.screen.blit(score_text, (10, 5))
