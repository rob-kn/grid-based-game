# This simulates the server side of storing the player information.
import configuration as conf
from server import Player
from server import Enemy
from server import Sprite
import random
from time import time


def is_tile_walkable(x_test, y_test):
    is_walkable = True
    if conf.COMPLETE_GRID[y_test][x_test] != ' ':
        is_walkable = False
    if (x_test, y_test) == (player1.x, player1.y):
        is_walkable = False
    for sprite in Sprite.sprites.values():
        if (sprite.x, sprite.y) == (x_test, y_test):
            is_walkable = False
    return is_walkable


def get_player():
    return player1


def set_player(p):
    # TODO lookup by id supplied as argument
    global player1
    player1 = p


def get_free_sides(center_x, center_y):
    free_tiles = []
    for xy in [(center_x-1, center_y),
               (center_x+1, center_y),
               (center_x, center_y+1),
               (center_x, center_y-1)]:
        if is_tile_walkable(xy[0], xy[1]):
            free_tiles.append((xy[0]-center_x, xy[1]-center_y))
    return free_tiles


def get_free_corners(center_x, center_y):
    free_tiles = []
    for xy in [(center_x-1, center_y-1),
               (center_x+1, center_y-1),
               (center_x-1, center_y+1),
               (center_x+1, center_y+1)]:
        if is_tile_walkable(xy[0], xy[1]):
            free_tiles.append((xy[0]-center_x, xy[1]-center_y))
    return free_tiles


def apply_random_movement(sprite):
    if sprite.offset == (0, 0):
        free_tiles = get_free_sides(sprite.x, sprite.y)
        if free_tiles:
            x_change, y_change = random.choice(free_tiles)
        elif get_free_corners(sprite.x, sprite.y):
            x_change, y_change = random.choice(get_free_corners(sprite.x, sprite.y))
        else:
            x_change, y_change = 0, 0
        sprite.reset_offset((sprite.x + x_change, sprite.y + y_change), (sprite.x, sprite.y))
        sprite.x = sprite.x + x_change
        sprite.y = sprite.y + y_change
    sprite.reduce_offset()


def update_sprites():
    ids_to_remove = []
    for sprite_id, sprite in Sprite.sprites.items():
        if sprite.sprite_type == "Enemy":
            apply_random_movement(sprite)
        if sprite.health <= 0:
            ids_to_remove.append(sprite_id)
    if ids_to_remove:
        Sprite.sprites = {key: value for key, value in Sprite.sprites.items() if key not in ids_to_remove}


def attack_sprites():
    global last_attack_time
    if time() - last_attack_time > player1.attack_speed:
        for sprite in Sprite.sprites.values():
            if sprite.sprite_id == player1.target:
                for x_change in range(-1, player1.range + 1):
                    for y_change in range(-1, player1.range + 1):
                        if player1.x + x_change == sprite.x and player1.y + y_change:
                            sprite.health -= player1.attack
        last_attack_time = time()


def get_sprites_around_xy(x_range, y_range):
    sprites_in_range = {}
    for sprite_id, sprite in Sprite.sprites.items():
        if sprite.x in x_range and sprite.y in y_range:
            sprites_in_range[sprite_id] = sprite
    return sprites_in_range


last_attack_time = time()
id_counter = 0

player1 = Player.Player(id_counter, "Player", 45, 9)
id_counter += 1
# Creates 15 randomly places enemies.

for i in range(15):
    x, y = random.randint(0, 80), random.randint(0, 20)
    while not is_tile_walkable(x, y):
        x, y = random.randint(0, 80), random.randint(0, 20)
    temp_enemy = Enemy.Enemy(id_counter, x, y, "giant_eye")
    id_counter += 1


