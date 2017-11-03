import pygame as pg
import configuration as conf


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

    def draw_camera_map(self, grid_x, grid_y, player):
        """
        Draws the map in the area around the player (or whatever x and y are given).
        Uses te offset value to shift the map to account for player movement.
        """
        self.player = player
        conf.screen.fill((0, 0, 0))
        range_x, range_y = self.get_onscreen_range(grid_x, grid_y)
        for col_count, y in enumerate(range_y):
            y_pixel = (col_count-1) * conf.GRID_SQUARE_SIZE
            for row_count, x in enumerate(range_x):
                x_pixel = (row_count-1) * conf.GRID_SQUARE_SIZE
                rect = pg.Rect(x_pixel + self.player.offset[0],
                               y_pixel + self.player.offset[1], conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
                conf.screen.blit(self.images[self.map[y][x]], rect)

    def get_onscreen_range(self, grid_x, grid_y):
        """
        This function takes an x and y and returns the ranges of tiles that should be drawn.
        It adds a 1 tile width border to account for any player movement.
        """
        range_x = range(grid_x - (self.center_to_xedge + 1), grid_x + (self.center_to_xedge + 1) + 1)
        range_y = range(grid_y - (self.center_to_yedge + 1), grid_y + (self.center_to_yedge + 1) + 1)
        return range_x, range_y

    def draw_entities(self, sprites):
        """
        Draws sprites, such as enemies, on the screen, relative to the player.
        The sprites are ordered so the top left is drawn first and the bottom right is drawn last.
        """
        for sprite in sorted(sprites.values(), key=lambda s: (s.x, s.y)):
            x_pixel = (((sprite.x - self.player.x) + self.center_x) - 1) * conf.GRID_SQUARE_SIZE
            y_pixel = (((sprite.y - self.player.y) + self.center_y) - 1) * conf.GRID_SQUARE_SIZE
            x_pixel = x_pixel + self.player.offset[0] - sprite.offset[0]
            y_pixel = y_pixel + self.player.offset[1] - sprite.offset[1]
            rect = pg.Rect(x_pixel, y_pixel, conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
            conf.screen.blit(sprite.image, rect)
            self.draw_sprite_name(x_pixel, y_pixel, sprite.name)
            self.draw_sprite_health_bar(x_pixel, y_pixel, sprite.health, sprite.max_health)
            if sprite.sprite_id == self.player.target:
                pg.draw.rect(conf.screen, conf.RED, (x_pixel, y_pixel, conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE), 3)

    def draw_sprite_name(self, x, y, name):
        name_text = conf.NAMES_FONT.render(name, 1, (255, 255, 255))
        text_width = name_text.get_rect().width
        text_spacing = (conf.GRID_SQUARE_SIZE - text_width) / 2
        conf.screen.blit(name_text, (x + text_spacing, y - 20))

    def draw_sprite_health_bar(self, x, y, health, max_health):
        health_percent = health / max_health
        health_pixels = int(health_percent * conf.GRID_SQUARE_SIZE)
        health_bar_color = conf.GREEN
        if health_percent < 0.6:
            health_bar_color = conf.YELLOW
        if health_percent < 0.3:
            health_bar_color = conf.RED
        pg.draw.rect(conf.screen, health_bar_color, (x, y - 10, health_pixels, 5), 0)


class Overlay:
    def __init__(self):
        self.font = conf.FONT

    def draw_overlay(self):
        score_text = self.font.render("Score - {0}".format(conf.SCORE), 1, (255, 255, 255))
        conf.screen.blit(score_text, (10, 5))

