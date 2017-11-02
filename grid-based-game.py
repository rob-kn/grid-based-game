import pygame as pg
import random
import configuration as conf
import server_sim as server
import draw_screen as draw_to_screen


def is_tile_walkable(x_test, y_test):
    return True if conf.COMPLETE_GRID[y_test][x_test] == ' ' else False


# def is_tile_this(x_test, y_test, test_tile):
#     return True if conf.COMPLETE_GRID[y_test][x_test] == test_tile else False
#

# # TODO: map should never be changed. Tiles should be an instance of a Tile class. (Create this)
# def change_tile(x_pos, y_pos, new_tile):
#     lst_row = list(conf.COMPLETE_GRID[y_pos])
#     lst_row[x_pos] = new_tile
#     conf.COMPLETE_GRID[y_pos] = ''.join(lst_row)
#
#
# def gen_target():
#     target_x, target_y = random.randint(0, conf.GRID_WIDTH - 1), random.randint(0, conf.GRID_HEIGHT - 1)
#
#     while not is_tile_walkable(target_x, target_y) \
#             and not is_tile_this(target_x, target_y, 'T') \
#             and (target_x, target_y) != (player.x, player.y):
#         target_x, target_y = random.randint(0, conf.GRID_WIDTH - 1), random.randint(0, conf.GRID_HEIGHT - 1)
#     change_tile(target_x, target_y, 'T')
#     print("Target created at ({}, {})".format(target_x, target_y))
#
#
# def change_targets(old_grid_pos):
#     # if old pos was T then it must be emptied, score updated and new T generated
#     if is_tile_this(old_grid_pos[0], old_grid_pos[1], 'T'):
#         change_tile(old_grid_pos[0], old_grid_pos[1], ' ')
#         conf.SCORE += 1
#         gen_target()


def update_grid_pos(old_grid_pos):
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
    # change_targets(old_grid_pos)
    return new_grid_pos


#gen_target()
camera = draw_to_screen.Camera(11, 13)
enemies = server.get_enemies()
while not conf.done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            conf.done = True

    # INPUT
    player = server.get_player()
    if player.offset == (0, 0):
        player.x, player.y = update_grid_pos((player.x, player.y))
    player.reduce_offset()
    server.set_player(player)
    # DRAW
    #draw_to_screen.draw_camera_view(player)
    camera.draw_camera_map(player.x, player.y, player.offset)
    camera.draw_player(player)
    camera.draw_entities(enemies)
    camera.draw_overlay()
    # UPDATE
    pg.display.flip()
    conf.clock.tick(conf.FPS)
