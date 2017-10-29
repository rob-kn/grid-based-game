import configuration as conf
import pygame as pg
import server_sim as server


def draw_camera_view():
    current_grid_pos = server.get_player_grid_pos(1)
    current_moving_offset = server.get_player_moving_offset(1)
    print(current_grid_pos)
    starting_x, starting_y = current_grid_pos[0] - 6, current_grid_pos[1] - 5
    print("Camera start point", starting_x, starting_y)
    conf.screen.fill((0, 0, 0))
    for y, row in enumerate(conf.COMPLETE_GRID[starting_y-1: starting_y+conf.CAMERA_HEIGHT+1]):
        for x, tile in enumerate(row[starting_x-1: starting_x+conf.CAMERA_WIDTH+1]):
            if tile == '#':
                pg.draw.rect(conf.screen, conf.BLUE,
                             pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                                     conf.GRID_SQUARE_SIZE))
            elif tile == ' ':
                pg.draw.rect(conf.screen, conf.BLACK,
                             pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                                     conf.GRID_SQUARE_SIZE))
            elif tile == 'T':
                pg.draw.rect(conf.screen, conf.RED,
                             pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                                     conf.GRID_SQUARE_SIZE))

    # this draws the player
    pg.draw.rect(conf.screen, conf.WHITE,
                 pg.Rect((conf.CENTER_X-1)*conf.GRID_SQUARE_SIZE, (conf.CENTER_Y-1)*conf.GRID_SQUARE_SIZE,
                         conf.GRID_SQUARE_SIZE,
                         conf.GRID_SQUARE_SIZE))
    # draw score
    score_text = conf.FONT.render("Score - {0}".format(conf.SCORE), 1, (255, 255, 255))
    conf.screen.blit(score_text, (10, 5))
