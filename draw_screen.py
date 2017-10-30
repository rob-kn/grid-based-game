import configuration as conf
import pygame as pg
import server_sim as server


def draw_camera_view():
    """
    This function will draw the current camera view of the game.
    It draws the relevant tiles only with a small overlap around the game window.
    It shifts the map by the current offset of the player.
    The player is always drawn in the center of the map.
    """
    current_grid_pos = server.get_player_grid_pos(1)
    current_moving_offset = server.get_player_moving_offset(1)
    # starting drawing points are off screen to allow for whichever direction the player is moving
    starting_x, starting_y = current_grid_pos[0] - conf.CENTER_X, current_grid_pos[1] - conf.CENTER_Y
    # This blanks the screen
    conf.screen.fill((0, 0, 0))
    # This loop draws the map around the player. It loops through with a 1 tile border.
    for y, row in enumerate(conf.COMPLETE_GRID[starting_y: starting_y+conf.CAMERA_HEIGHT+2]):
        for x, tile in enumerate(row[starting_x: starting_x+conf.CAMERA_WIDTH+2]):
            if tile == '#':
                # pg.draw.rect(conf.screen, conf.BLUE,
                #              pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                #                      conf.GRID_SQUARE_SIZE))
                wall_rect = pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                                      conf.GRID_SQUARE_SIZE)
                conf.screen.blit(conf.wall_img, wall_rect)
            elif tile == ' ':
                # pg.draw.rect(conf.screen, conf.BLACK,
                #              pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                #                      conf.GRID_SQUARE_SIZE))
                floor_rect = pg.Rect(((x - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[0],
                        ((y - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                        conf.GRID_SQUARE_SIZE)
                conf.screen.blit(conf.floor_img, floor_rect)
            elif tile == 'T':
                # pg.draw.rect(conf.screen, conf.RED,
                #              pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                #                      conf.GRID_SQUARE_SIZE))
                floor_rect = pg.Rect(((x - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[0],
                                     ((y - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[1],
                                     conf.GRID_SQUARE_SIZE,
                                     conf.GRID_SQUARE_SIZE)
                conf.screen.blit(conf.floor_img, floor_rect)
                strawb_rect = pg.Rect(((x - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[0],
                    ((y - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                    conf.GRID_SQUARE_SIZE)
                conf.screen.blit(conf.strawb_img, strawb_rect)

    # This draws the player
    # pg.draw.rect(conf.screen, conf.WHITE,
    #              pg.Rect((conf.CENTER_X-1)*conf.GRID_SQUARE_SIZE, (conf.CENTER_Y-1)*conf.GRID_SQUARE_SIZE,
    #                      conf.GRID_SQUARE_SIZE,
    #                      conf.GRID_SQUARE_SIZE))
    player_rect = pg.Rect((conf.CENTER_X - 1) * conf.GRID_SQUARE_SIZE, (conf.CENTER_Y - 1) * conf.GRID_SQUARE_SIZE,
                                  conf.GRID_SQUARE_SIZE,
                                  conf.GRID_SQUARE_SIZE)
    conf.screen.blit(conf.player_img, player_rect)
    # This draws the score count
    score_text = conf.FONT.render("Score - {0}".format(conf.SCORE), 1, (255, 255, 255))
    conf.screen.blit(score_text, (10, 5))
