import pygame as pg
import random
import configuration as conf
import server_sim as server
import draw_screen as draw_to_screen


def is_tile_walkable(x_test, y_test):
    return True if conf.COMPLETE_GRID[y_test][x_test] == ' ' or conf.COMPLETE_GRID[y_test][x_test] == 'T' else False


def is_tile_this(x_test, y_test, test_tile):
    return True if conf.COMPLETE_GRID[y_test][x_test] == test_tile else False


def change_tile(x_pos, y_pos, new_tile):
    lst_row = list(conf.COMPLETE_GRID[y_pos])
    lst_row[x_pos] = new_tile
    conf.COMPLETE_GRID[y_pos] = ''.join(lst_row)


def gen_target():
    target_x, target_y = random.randint(0, conf.GRID_WIDTH - 1), random.randint(0, conf.GRID_HEIGHT - 1)

    while not is_tile_walkable(target_x, target_y) \
            and not is_tile_this(target_x, target_y, 'T') \
            and (target_x, target_y) != server.get_player_grid_pos(1):
        target_x, target_y = random.randint(0, conf.GRID_WIDTH - 1), random.randint(0, conf.GRID_HEIGHT - 1)
    change_tile(target_x, target_y, 'T')
    print("Target created at ({}, {})".format(target_x, target_y))


def change_targets(old_grid_pos):
    # if old pos was T then it must be emptied, score updated and new T generated
    if is_tile_this(old_grid_pos[0], old_grid_pos[1], 'T'):
        change_tile(old_grid_pos[0], old_grid_pos[1], ' ')
        conf.SCORE += 1
        gen_target()


def update_grid_pos(old_grid_pos):
    new_grid_x, new_grid_y = old_grid_pos
    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]:
        if is_tile_walkable(new_grid_x, new_grid_y - 1):
            new_grid_y -= 1
    if pressed[pg.K_DOWN]:
        if is_tile_walkable(new_grid_x, new_grid_y + 1):
            new_grid_y += 1
    if pressed[pg.K_LEFT]:
        if is_tile_walkable(new_grid_x - 1, new_grid_y):
            new_grid_x -= 1
    if pressed[pg.K_RIGHT]:
        if is_tile_walkable(new_grid_x + 1, new_grid_y):
            new_grid_x += 1
    new_grid_x = min(conf.GRID_WIDTH - 1, max(new_grid_x, 0))
    new_grid_y = min(conf.GRID_HEIGHT - 1, max(new_grid_y, 0))
    new_grid_pos = (new_grid_x, new_grid_y)
    update_offset(1, new_grid_pos, old_grid_pos)
    change_targets(old_grid_pos)
    return new_grid_pos


def update_offset(player_id, new_grid_pos, old_grid_pos):
    new_offset_x = 0
    new_offset_y = 0
    new_offset_x = -conf.GRID_SQUARE_SIZE if new_grid_pos[0] < old_grid_pos[0] else new_offset_x
    new_offset_x = +conf.GRID_SQUARE_SIZE if new_grid_pos[0] > old_grid_pos[0] else new_offset_x
    new_offset_y = -conf.GRID_SQUARE_SIZE if new_grid_pos[1] < old_grid_pos[1] else new_offset_y
    new_offset_y = +conf.GRID_SQUARE_SIZE if new_grid_pos[1] > old_grid_pos[1] else new_offset_y
    server.set_player_moving_offset(player_id, (new_offset_x, new_offset_y))
    # print(new_offset_x, new_offset_y)


def reduce_offset(player_id):
    # gets current offset and converges it to zero.
    # TODO: Offsets can be stored locally (not from server)
    current_offset_x, current_offset_y = server.get_player_moving_offset(1)
    if current_offset_x > 0:
        current_offset_x -= 2
    if current_offset_x < 0:
        current_offset_x += 2
    if current_offset_y > 0:
        current_offset_y -= 2
    if current_offset_y < 0:
        current_offset_y += 2
    server.set_player_moving_offset(1, (current_offset_x, current_offset_y))
    print(current_offset_x, current_offset_y) if current_offset_x != 0 or current_offset_y != 0 else None


gen_target()
while not conf.done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            conf.done = True

    # INPUT
    if server.get_player_moving_offset(1) == (0, 0):
        server.set_player_grid_pos(1, update_grid_pos(server.get_player_grid_pos(1)))
    reduce_offset(1)
    # DRAW
    draw_to_screen.draw_camera_view()

    # UPDATE
    pg.display.flip()
    conf.clock.tick(conf.FPS)
