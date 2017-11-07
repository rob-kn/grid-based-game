import pygame as pg
import configuration as conf
import random
from time import time


class Camera:
    def __init__(self):
        self.height = conf.CAMERA_HEIGHT
        self.width = conf.CAMERA_WIDTH
        self.camera_startx = conf.CAMERA_STARTX
        self.camera_starty = conf.CAMERA_STARTY
        self.center_to_xedge = int((self.width - 1) / 2)  # 5
        self.center_to_yedge = int((self.height - 1) / 2)  # 6
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
            y_pixel = (col_count - 1) * conf.GRID_SQUARE_SIZE + self.player.offset[1]
            y_pixel += self.camera_starty
            for row_count, x in enumerate(range_x):
                x_pixel = (row_count - 1) * conf.GRID_SQUARE_SIZE + self.player.offset[0]
                x_pixel += self.camera_startx
                rect = pg.Rect(x_pixel, y_pixel, conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
                conf.screen.blit(self.images[self.map[y][x]], rect)

    def draw_items(self, items):
        for item_id, item in items.items():
            x_pixel, y_pixel = get_rel_pos_on_camera(self.player, item, self)
            rect = pg.Rect(x_pixel, y_pixel, conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
            conf.screen.blit(item.image, rect)

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
        for sprite in sorted(sprites.values(),
                             key=lambda s: ((s.x * conf.GRID_SQUARE_SIZE) + s.offset[0] + self.player.offset[0],
                                            (s.y * conf.GRID_SQUARE_SIZE) + s.offset[1] + self.player.offset[1])):
            x_pixel, y_pixel = get_rel_pos_on_camera(self.player, sprite, self)
            rect = pg.Rect(x_pixel, y_pixel, conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE)
            for layer in sprite.images:
                conf.screen.blit(layer, rect)

    def draw_health_and_names(self, sprites):
        for sprite in sorted(sprites.values(),
                             key=lambda s: ((s.x * conf.GRID_SQUARE_SIZE) + s.offset[0] + self.player.offset[0],
                                            (s.y * conf.GRID_SQUARE_SIZE) + s.offset[1] + self.player.offset[1])):
            x_pixel, y_pixel = get_rel_pos_on_camera(self.player, sprite, self)
            draw_sprite_name(x_pixel, y_pixel, sprite.name)
            draw_health_bar(x_pixel, y_pixel - 10, sprite.health, sprite.max_health, conf.GRID_SQUARE_SIZE, 5)
            if sprite.sprite_id == self.player.target:
                pg.draw.rect(conf.screen, conf.RED, (x_pixel, y_pixel, conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE), 3)


def draw_sprite_name(x, y, name):
    name_text = conf.NAMES_FONT.render(name, 1, conf.WHITE)
    text_width = name_text.get_rect().width
    text_spacing = (conf.GRID_SQUARE_SIZE - text_width) / 2
    conf.screen.blit(name_text, (x + text_spacing, y - 20))


def draw_health_bar(x, y, health, max_health, max_width, thickness):
    health_percent = health / max_health
    health_pixels = int(health_percent * max_width)
    health_bar_color = conf.GREEN
    if health_percent < 0.6:
        health_bar_color = conf.YELLOW
    if health_percent < 0.3:
        health_bar_color = conf.RED
    pg.draw.rect(conf.screen, health_bar_color, (x, y, health_pixels, thickness), 0)


def draw_mana_bar(x, y, mana, max_mana, max_width, thickness):
    mana_percent = mana / max_mana
    mana_pixels = int(mana_percent * max_width)
    mana_bar_color = conf.BLUE
    pg.draw.rect(conf.screen, mana_bar_color, (x, y, mana_pixels, thickness), 0)


def get_rel_pos_on_camera(relative_player, sprite, camera):
    x_pixel = (((sprite.x - relative_player.x) + camera.center_x) - 1) * conf.GRID_SQUARE_SIZE
    y_pixel = (((sprite.y - relative_player.y) + camera.center_y) - 1) * conf.GRID_SQUARE_SIZE
    x_pixel += relative_player.offset[0] - sprite.offset[0]
    y_pixel += relative_player.offset[1] - sprite.offset[1]
    x_pixel += camera.camera_startx
    y_pixel += camera.camera_starty
    return x_pixel, y_pixel


class Overlay:
    def __init__(self):
        self.font48 = conf.FONT_48
        self.font32 = conf.FONT_32
        self.font32_bold = conf.FONT_32_BOLD
        self.font16 = conf.FONT_16
        self.left_pane_width = conf.LEFT_PANE_WIDTH
        self.left_pane_startx = conf.LEFT_PANE_STARTX
        self.left_pane_starty = conf.LEFT_PANE_STARTY
        self.left_pane_border_width = 5
        self.right_pane_width = conf.RIGHT_PANE_WIDTH
        self.right_pane_startx = conf.RIGHT_PANE_STARTX
        self.right_pane_starty = conf.RIGHT_PANE_STARTY
        self.y_spacing = 5
        self.player = None

    def draw_left_pane(self, player):
        self.player = player
        # For player info / stats

        # Draw background
        pg.draw.rect(conf.screen, conf.GREY, (self.left_pane_startx, self.left_pane_starty,
                                              self.left_pane_width, conf.SCREEN_HEIGHT), 0)

        # Draw border
        pg.draw.rect(conf.screen, conf.SLATE_GREY, (self.left_pane_startx, self.left_pane_starty,
                                                    self.left_pane_width, conf.SCREEN_HEIGHT),
                     self.left_pane_border_width)

        # Draw player name, lvl and exp, hp and mp bars
        pname_end_y = self.draw_pname(self.left_pane_startx + self.left_pane_border_width,
                                      self.left_pane_starty + self.left_pane_border_width)

        lvl_exp_end_y = self.draw_lvl_exp(self.left_pane_startx + self.left_pane_border_width, pname_end_y)
        self.draw_lvlup(conf.CAMERA_WIDTH_PIXELS / 2 + self.left_pane_width, 20)

        hp_mp_end_y = self.draw_hp_mp_bars(self.left_pane_startx + self.left_pane_border_width, lvl_exp_end_y)

        # Draw equipment

    def draw_pname(self, x, y):
        name_text = self.font48.render(self.player.name, 1, conf.WHITE)
        name_text_width = name_text.get_rect().width
        name_text_spacing = (self.left_pane_width - name_text_width) / 2
        conf.screen.blit(name_text, (x + name_text_spacing, y + self.y_spacing))
        pg.draw.rect(conf.screen, conf.SLATE_GREY,
                     (0, y + self.y_spacing + name_text.get_rect().height + self.y_spacing,
                      self.left_pane_width, 4), 0)
        end_y = y + self.y_spacing + name_text.get_rect().height + self.y_spacing + 4
        return end_y

    def draw_hp_mp_bars(self, x, y):
        hp_text = conf.FONT_32.render("Health", 1, conf.WHITE)
        hp_stats = conf.FONT_32.render("{:>5}/{:<5}".format(self.player.health, self.player.max_health), 1, conf.WHITE)
        conf.screen.blit(hp_text, (x + 5, y + self.y_spacing))
        conf.screen.blit(hp_stats, (
            self.left_pane_width - (self.left_pane_border_width + 5 + hp_stats.get_rect().width), y + self.y_spacing))
        end_y = y + self.y_spacing + hp_text.get_rect().height + self.y_spacing
        pg.draw.rect(conf.screen, conf.SLATE_GREY,
                     (0, end_y,
                      self.left_pane_width, 4), 0)
        end_y += self.y_spacing + 4
        draw_health_bar(x + 5, end_y, self.player.health, self.player.max_health,
                        self.left_pane_width - (x + 10 + 2*self.left_pane_border_width), hp_text.get_rect().height)
        end_y += hp_text.get_rect().height + self.y_spacing
        pg.draw.rect(conf.screen, conf.SLATE_GREY,
                     (0, end_y,
                      self.left_pane_width, 4), 0)
        end_y += 4

        mp_text = conf.FONT_32.render("Mana", 1, conf.WHITE)
        mp_stats = conf.FONT_32.render("{:>5}/{:<5}".format(self.player.mana, self.player.max_mana), 1, conf.WHITE)
        conf.screen.blit(mp_text, (x + 5, end_y + self.y_spacing))
        conf.screen.blit(mp_stats, (
            self.left_pane_width - (self.left_pane_border_width + 5 + mp_stats.get_rect().width), end_y + self.y_spacing))
        end_y += self.y_spacing + mp_text.get_rect().height + self.y_spacing
        pg.draw.rect(conf.screen, conf.SLATE_GREY,
                     (0, end_y,
                      self.left_pane_width, 4), 0)
        end_y += self.y_spacing + 4
        draw_mana_bar(x + 5, end_y, self.player.mana, self.player.max_mana,
                        self.left_pane_width - (x + 10 + 2 * self.left_pane_border_width), mp_text.get_rect().height)
        end_y += hp_text.get_rect().height + self.y_spacing
        pg.draw.rect(conf.screen, conf.SLATE_GREY,
                     (0, end_y,
                      self.left_pane_width, 4), 0)
        end_y += 4
        return end_y

    def draw_lvl_exp(self, x, y):
        level_exp_text = self.font32.render("Level {:<5} Exp {:<5}".format(self.player.player_level, self.player.exp), 1,
                                            conf.WHITE)
        level_text_width = level_exp_text.get_rect().width
        level_text_spacing = (self.left_pane_width - level_text_width) / 2
        conf.screen.blit(level_exp_text,
                         (x + level_text_spacing, y + self.y_spacing))
        end_y = y + self.y_spacing + level_exp_text.get_rect().height + self.y_spacing
        pg.draw.rect(conf.screen, conf.SLATE_GREY,
                     (0, end_y,
                      self.left_pane_width, 4), 0)
        end_y += 4
        return end_y

    def draw_lvlup(self, x, y):
        if self.player.last_level_up_time + 5 > time():
            lvlup_text = self.font48.render("LEVEL UP TO {}!".format(self.player.player_level), 1, conf.GREEN)
            lvlup_text_width = lvlup_text.get_rect().width
            conf.screen.blit(lvlup_text, (x - lvlup_text_width/2, y))
            self.draw_up_arrow(x+lvlup_text_width + 10, y)
            self.draw_up_arrow(x-(lvlup_text_width + 10), y)

    def draw_up_arrow(self, x, y):
        pg.draw.polygon(conf.screen, conf.GREEN, ((x, y), (x+20, y+20), (x+10, y+20), (x+10, y+40),
                                                  (x-10, y+40), (x-10, y+20), (x-20, y+20), (x, y)), 0)

    def draw_right_pane(self):
        pg.draw.rect(conf.screen, conf.GREY, (self.right_pane_startx, self.right_pane_starty,
                                              self.right_pane_width, conf.SCREEN_HEIGHT), 0)
        pg.draw.rect(conf.screen, conf.SLATE_GREY, (self.right_pane_startx, self.right_pane_starty,
                                                    self.right_pane_width, conf.SCREEN_HEIGHT), 5)
        inventory_text = self.font32.render("Inventory", 1, (255, 255, 255))
        text_width = inventory_text.get_rect().width
        text_spacing = (self.right_pane_width - text_width) / 2
        conf.screen.blit(inventory_text, (self.right_pane_startx + text_spacing, self.right_pane_starty))
