import pygame as pg

import configuration as conf
import Rendering as render
from server import Server_main as server


def is_tile_walkable(x_test, y_test):
    is_walkable = True
    if conf.COMPLETE_GRID[y_test][x_test] != ' ':
        is_walkable = False
    if (x_test, y_test) == (player.x, player.y):
        is_walkable = False
    for sprite in sprites:
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
            print(x_pixel, y_pixel)
            x_pos = int(x_pixel / conf.GRID_SQUARE_SIZE) + 1
            y_pos = int(y_pixel / conf.GRID_SQUARE_SIZE) + 1
            print(x_pos, y_pos)
            rel_x_pos = x_pos - camera.center_x
            rel_y_pos = y_pos - camera.center_y
            print(rel_x_pos, rel_y_pos)
            grid_x = rel_x_pos + player.x
            grid_y = rel_y_pos + player.y
            print(grid_x, grid_y)
            for sprite in sprites:
                if sprite.x == grid_x and sprite.y == grid_y:
                    player.target = sprite.sprite_id
        if event.type == pg.MOUSEBUTTONUP:
            print(pg.mouse.get_pos())


camera = render.Camera(11, 13)
overlay = render.Overlay()
while not conf.done:

    # INPUT
    player = server.get_player()
    x_range = range(player.x - (camera.center_to_xedge + 2), player.x + (camera.center_to_xedge + 2))
    y_range = range(player.y - (camera.center_to_yedge + 2), player.y + (camera.center_to_yedge + 2))
    sprites = server.get_sprites_around_xy(x_range, y_range)
    server.update_sprites()
    if player.offset == (0, 0):
        player.x, player.y = update_grid_pos((player.x, player.y))
    player.reduce_offset()

    detect_events()

    # Update player
    server.set_player(player)

    # DRAW
    camera.draw_camera_map(player.x, player.y, player)
    camera.draw_entities(sprites)
    overlay.draw_overlay()
    # UPDATE
    pg.display.flip()
    conf.clock.tick(conf.FPS)
