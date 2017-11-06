import pygame as pg
from time import time

import configuration as conf
import Rendering as render
from server import Server_main as server


def is_tile_walkable(x_test, y_test):
    is_walkable = True
    if conf.COMPLETE_GRID[y_test][x_test] != ' ':
        is_walkable = False
    if (x_test, y_test) == (player.x, player.y):
        is_walkable = False
    for sprite in sprites.values():
        if (sprite.x, sprite.y) == (x_test, y_test):
            is_walkable = False
    return is_walkable


def update_grid_pos(old_grid_pos):
    global player
    new_grid_x, new_grid_y = old_grid_pos
    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]:
        new_grid_y -= 1
    if pressed[pg.K_DOWN]:
        new_grid_y += 1
    if pressed[pg.K_LEFT]:
        new_grid_x -= 1
    if pressed[pg.K_RIGHT]:
        new_grid_x += 1
    if not is_tile_walkable(new_grid_x, new_grid_y):
        if is_tile_walkable(new_grid_x, old_grid_pos[1]):
            new_grid_y = old_grid_pos[1]
        elif is_tile_walkable(old_grid_pos[0], new_grid_y):
            new_grid_x = old_grid_pos[0]
        else:
            new_grid_x, new_grid_y = old_grid_pos
    new_grid_pos = (new_grid_x, new_grid_y)
    player.reset_offset(new_grid_pos, old_grid_pos)
    return new_grid_pos


def detect_events():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            conf.done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            x_pixel, y_pixel = pg.mouse.get_pos()
            for sprite in sprites.values():
                sprite_x_pixel = (((sprite.x - player.x) + camera.center_x) - 1) * conf.GRID_SQUARE_SIZE
                sprite_y_pixel = (((sprite.y - player.y) + camera.center_y) - 1) * conf.GRID_SQUARE_SIZE
                sprite_x_pixel += player.offset[0] - sprite.offset[0]
                sprite_y_pixel += player.offset[1] - sprite.offset[1]
                sprite_x_pixel += camera.camera_startx
                sprite_y_pixel += camera.camera_starty
                if sprite_x_pixel < x_pixel < sprite_x_pixel + conf.GRID_SQUARE_SIZE:
                    if sprite_y_pixel < y_pixel < sprite_y_pixel + conf.GRID_SQUARE_SIZE:
                        player.target = sprite.sprite_id if player.target != sprite.sprite_id else None
        if event.type == pg.MOUSEBUTTONUP:
            # print(pg.mouse.get_pos())
            pass


camera = render.Camera()
overlay = render.Overlay()
while not conf.done:

    # INPUT
    player = server.get_player()
    x_range = range(player.x - (camera.center_to_xedge + 2), player.x + (camera.center_to_xedge + 2))
    y_range = range(player.y - (camera.center_to_yedge + 2), player.y + (camera.center_to_yedge + 2))
    sprites = server.get_sprites_around_xy(x_range, y_range)
    server.update_sprites()
    items = server.get_items_around_xy(x_range, y_range)

    if player.offset == (0, 0):
        player.x, player.y = update_grid_pos((player.x, player.y))
    player.reduce_offset()

    detect_events()

    # Update player
    server.set_player(player)

    # DRAW
    camera.draw_camera_map(player.x, player.y, player)
    camera.draw_items(items)
    camera.draw_entities(sprites)
    overlay.draw_overlay()
    overlay.draw_left_pane(player)
    overlay.draw_right_pane()
    # UPDATE
    pg.display.flip()
    conf.clock.tick(conf.FPS)
