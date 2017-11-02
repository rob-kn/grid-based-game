import pygame as pg

import configuration as conf
import draw_screen as draw_to_screen
from server import Server_main as server


def is_tile_walkable(x_test, y_test):
    is_walkable = True
    if conf.COMPLETE_GRID[y_test][x_test] != ' ':
        is_walkable = False
    if (x_test, y_test) == (player.x, player.y):
        is_walkable = False
    for enemy in enemies:
        if (enemy.x, enemy.y) == (x_test, y_test):
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
    new_grid_x = min(conf.GRID_WIDTH - 1, max(new_grid_x, 0))
    new_grid_y = min(conf.GRID_HEIGHT - 1, max(new_grid_y, 0))
    new_grid_pos = (new_grid_x, new_grid_y)
    player.reset_offset(new_grid_pos, old_grid_pos)
    return new_grid_pos


camera = draw_to_screen.Camera(11, 13)
while not conf.done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            conf.done = True

    # INPUT
    player = server.get_player()
    enemies = server.get_enemies()
    if player.offset == (0, 0):
        player.x, player.y = update_grid_pos((player.x, player.y))
    player.reduce_offset()
    server.set_player(player)

    # DRAW
    camera.draw_camera_map(player.x, player.y, player.offset)
    camera.draw_player(player)
    camera.draw_entities(enemies)
    camera.draw_overlay()
    # UPDATE
    pg.display.flip()
    conf.clock.tick(conf.FPS)
