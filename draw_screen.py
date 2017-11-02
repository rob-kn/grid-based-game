import pygame as pg

import configuration as conf


#TODO : split into draw_map_camera(camx, camy) and draw_entities() (both funcs of a class)


class Camera:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.center_to_xedge = int((self.width - 1) / 2)     # 5
        self.center_to_yedge = int((self.height - 1) / 2)    # 6
        self.center_x = self.width - self.center_to_xedge
        self.center_y = self.height - self.center_to_yedge
        self.map = [line.strip() for line in open('maps/level_0_map.txt').readlines()]
        self.images = {'#': conf.wall_img,
                       ' ': conf.floor_img}
        self.player = None

    def draw_camera_map(self, grid_x, grid_y, offset):
        conf.screen.fill((0, 0, 0))
        range_x, range_y = self.get_onscreen_range(grid_x, grid_y, offset)
        for col_count, y in enumerate(range_y):
            y_pixel = (col_count-1) * conf.GRID_SQUARE_SIZE
            for row_count, x in enumerate(range_x):
                x_pixel = (row_count-1) * conf.GRID_SQUARE_SIZE
                rect = pg.Rect(x_pixel + offset[0], y_pixel + offset[1], conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
                conf.screen.blit(self.images[self.map[y][x]], rect)


    def get_onscreen_range(self, grid_x, grid_y, offset):
        """
        This function takes an x and y and returns the ranges of tiles that should be drawn.
        It adds a 1 tile border to account for any player movement.
        """
        range_x = range(grid_x - (self.center_to_xedge + 1), grid_x + (self.center_to_xedge + 1) + 1)
        range_y = range(grid_y - (self.center_to_yedge + 1), grid_y + (self.center_to_yedge + 1) + 1)
        return range_x, range_y

    def draw_player(self, player):
        self.player = player
        rect = pg.Rect((self.center_x - 1)*conf.GRID_SQUARE_SIZE, (self.center_y-1)*conf.GRID_SQUARE_SIZE,
                       conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
        conf.screen.blit(conf.player_img, rect)

    def draw_entities(self, entities):
        for entity in entities:
            relative_x_pixel = (((entity.x - self.player.x) + self.center_x) - 1) * conf.GRID_SQUARE_SIZE
            relative_y_pixel = (((entity.y - self.player.y) + self.center_y) - 1) * conf.GRID_SQUARE_SIZE
            rect = pg.Rect(relative_x_pixel + self.player.offset[0] - entity.offset[0],
                           relative_y_pixel + self.player.offset[1] - entity.offset[1],
                           conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
            conf.screen.blit(entity.image, rect)

    def draw_overlay(self):
        # TODO can be own class where fonts / overlap images are stored
        score_text = conf.FONT.render("Score - {0}".format(conf.SCORE), 1, (255, 255, 255))
        conf.screen.blit(score_text, (10, 5))

