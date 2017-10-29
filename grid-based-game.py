import pygame as pg
import random
import configuration as conf
import server_sim as server
import draw_screen as draw_to_screen


def is_tile_walkable(x_test, y_test):
    return True if conf.GRID_DESIGN[y_test][x_test] == ' ' or conf.GRID_DESIGN[y_test][x_test] == 'T' else False


def is_tile_this(x_test, y_test, test_tile):
    return True if conf.GRID_DESIGN[y_test][x_test] == test_tile else False


def change_tile(x_pos, y_pos, new_tile):
    lst_row = list(conf.GRID_DESIGN[y_pos])
    lst_row[x_pos] = new_tile
    conf.GRID_DESIGN[y_pos] = ''.join(lst_row)


def gen_target():
    target_x, target_y = random.randint(0, 9), random.randint(0, 9)
    while not is_tile_walkable(target_x, target_y) and not is_tile_this(target_x, target_y, 'T') and (
            target_x, target_y) != server.get_player_grid_pos(1):
        target_x, target_y = random.randint(0, 9), random.randint(0, 9)
    change_tile(target_x, target_y, 'T')
    print("Target created at ({}, {})".format(target_x, target_y))


def change_targets(old_grid_pos):
    # if old pos was T then it must be emptied and score updated
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
    new_grid_x = min(conf.GRID_WIDTH, max(new_grid_x, 0))
    new_grid_y = min(conf.GRID_HEIGHT, max(new_grid_y, 0))
    new_grid_pos = (new_grid_x, new_grid_y)

    change_targets(old_grid_pos)
    return new_grid_pos


def update_movement(screen_pos, grid_pos):
    screen_x, screen_y = screen_pos
    if screen_x < grid_pos[0] * conf.GRID_SQUARE_SIZE:
        screen_x += 2
    elif screen_x > grid_pos[0] * conf.GRID_SQUARE_SIZE:
        screen_x -= 2
    if screen_y < grid_pos[1] * conf.GRID_SQUARE_SIZE:
        screen_y += 2
    elif screen_y > grid_pos[1] * conf.GRID_SQUARE_SIZE:
        screen_y -= 2
    screen_x = min(conf.WINDOW_WIDTH - conf.GRID_SQUARE_SIZE, max(0, screen_x))
    screen_y = min(conf.WINDOW_HEIGHT - conf.GRID_SQUARE_SIZE, max(0, screen_y))
    return screen_x, screen_y


gen_target()
while not conf.done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            conf.done = True

    # INPUT
    if tuple([i * conf.GRID_SQUARE_SIZE for i in server.get_player_grid_pos(1)]) == server.get_player_moving_pos(1):
        server.set_player_grid_pos(1, update_grid_pos(server.get_player_grid_pos(1)))
    server.set_player_moving_pos(1, update_movement(server.get_player_moving_pos(1), server.get_player_grid_pos(1)))

    # DRAW
    draw_to_screen.draw_game()

    # UPDATE
    pg.display.flip()
    conf.clock.tick(conf.FPS)
