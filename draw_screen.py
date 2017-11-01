import configuration as conf
import pygame as pg
import server_sim as server

#TODO : split into draw_map_camera(camx, camy) and draw_entities() (both funcs of a class)

class Camera:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = [line.strip() for line in open('maps/level_0_map.txt').readlines()]

    def draw_camera_map(self, cam_x, cam_y):
        for y in range(self.height):
            for x in range(self.width):
                tile_position_x = (x * conf.TILE_WIDTH) - cam_x
                tile_position_y = (y * conf.TILE_HEIGHT) - cam_y
                if onscreen(tile_position_x, tile_position_y):
                    self.map[y][x].draw(conf.screen, x * conf.TILE_WIDTH, y * conf.TILE_HEIGHT)

    def on_screen(self, x, y):
        return not (x < conf.GRID_SQUARE_SIZE or x > conf.SCREEN_WIDTH or
                    y < conf.GRID_SQUARE_SIZE or y > conf.SCREEN_HEIGHT)

def draw_camera_view(player):
    """
    This function will draw the current camera view of the game.
    It draws the relevant tiles only with a small overlap around the game window.
    It shifts the map by the current offset of the player.
    The player is always drawn in the center of the map.
    """
    current_grid_pos = (player.x, player.y)
    current_moving_offset = player.offset

    # starting drawing points are off screen to allow for whichever direction the player is moving
    starting_x, starting_y = current_grid_pos[0] - conf.CENTER_X, current_grid_pos[1] - conf.CENTER_Y
    # This blanks the screen
    conf.screen.fill((0, 0, 0))
    # This loop draws the map around the player. It loops through with a 1 tile border.
    for y, row in enumerate(conf.COMPLETE_GRID[starting_y: starting_y+conf.CAMERA_HEIGHT+2]):
        for x, tile in enumerate(row[starting_x: starting_x+conf.CAMERA_WIDTH+2]):
            if tile == '#':
                wall_rect = pg.Rect(((x-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[0], ((y-1) * conf.GRID_SQUARE_SIZE)+current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                                      conf.GRID_SQUARE_SIZE)
                conf.screen.blit(conf.wall_img, wall_rect)
            elif tile == ' ':
                floor_rect = pg.Rect(((x - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[0],
                        ((y - 1) * conf.GRID_SQUARE_SIZE) + current_moving_offset[1], conf.GRID_SQUARE_SIZE,
                        conf.GRID_SQUARE_SIZE)
                conf.screen.blit(conf.floor_img, floor_rect)
            elif tile == 'T':
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
    player_rect = pg.Rect((conf.CENTER_X - 1) * conf.GRID_SQUARE_SIZE, (conf.CENTER_Y - 1) * conf.GRID_SQUARE_SIZE,
                                  conf.GRID_SQUARE_SIZE,
                                  conf.GRID_SQUARE_SIZE)
    conf.screen.blit(conf.player_img, player_rect)
    # This draws the score count
    score_text = conf.FONT.render("Score - {0}".format(conf.SCORE), 1, (255, 255, 255))
    conf.screen.blit(score_text, (10, 5))
