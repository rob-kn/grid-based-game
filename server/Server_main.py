# This simulates the server side of storing the player information.
import configuration as conf
from server import Player
from server import Enemy
from server import Sprite
import random


def is_tile_walkable(x_test, y_test):
    is_walkable = True
    if conf.COMPLETE_GRID[y_test][x_test] != ' ':
        is_walkable = False
    if (x_test, y_test) == (player1.x, player1.y):
        is_walkable = False
    for sprite in Sprite.sprites:
        if (sprite.x, sprite.y) == (x_test, y_test):
            is_walkable = False
    return is_walkable


def get_player():
    return player1


def set_player(p):
    # TODO lookup by id supplied as argument
    global player1
    player1 = p


def get_enemies():
    for enemy in Enemy.enemies:
        if enemy.offset == (0, 0):
            free_tiles = get_free_tiles(enemy.x, enemy.y)
            if free_tiles:
                x_change, y_change = random.choice(free_tiles)
            else:
                x_change, y_change = 0, 0
            enemy.reset_offset((enemy.x + x_change, enemy.y + y_change), (enemy.x, enemy.y))
            enemy.x = enemy.x + x_change
            enemy.y = enemy.y + y_change
        enemy.reduce_offset()
    return Enemy.enemies


def get_free_tiles(center_x, center_y):
    free_tiles = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if is_tile_walkable(center_x + x, center_y + y):
                free_tiles.append((x, y))
    return free_tiles


def apply_random_movement(sprite):
    if sprite.offset == (0, 0):
        free_tiles = get_free_tiles(sprite.x, sprite.y)
        if free_tiles:
            x_change, y_change = random.choice(free_tiles)
        else:
            x_change, y_change = 0, 0
        sprite.reset_offset((sprite.x + x_change, sprite.y + y_change), (sprite.x, sprite.y))
        sprite.x = sprite.x + x_change
        sprite.y = sprite.y + y_change
    sprite.reduce_offset()


def update_sprites():
    for sprite in Sprite.sprites:
        if sprite.sprite_type == "Enemy":
            apply_random_movement(sprite)


def get_sprites_around_xy(center_x, center_y, x_range, y_range):
    sprites_in_range = []
    for sprite in Sprite.sprites:
        if sprite.x in x_range and sprite.y in y_range:
            sprites_in_range.append(sprite)
    return sprites_in_range



player1 = Player.Player("Player", 1, 45, 9)
# Creates 15 randomly places enemies.
for i in range(15):
    x, y = random.randint(0, 80), random.randint(0, 20)
    while not is_tile_walkable(x, y):
        x, y = random.randint(0, 80), random.randint(0, 20)
    temp_enemy = Enemy.Enemy(1, x, y, "giant_eye")


