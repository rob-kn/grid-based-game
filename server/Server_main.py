# This simulates the server side of storing the player information.
import configuration as conf
from server import Player
from server import Enemy
from server import Sprite
from server import Item
import random


def is_tile_walkable(x_test, y_test, sprite_id):
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
    # TODO lookup by id supplied as argument or send a requent from client to move in a certain position,
    # server then double checks to see if valid before making changes (to move towards only server changing player)
    global player1
    player1 = p


def get_free_sides(center_x, center_y):
    free_tiles = []
    for xy in [(center_x - 1, center_y),
               (center_x + 1, center_y),
               (center_x, center_y + 1),
               (center_x, center_y - 1)]:
        if is_tile_walkable(xy[0], xy[1], None):
            free_tiles.append((xy[0] - center_x, xy[1] - center_y))
    return free_tiles


def get_free_corners(center_x, center_y):
    free_tiles = []
    for xy in [(center_x - 1, center_y - 1),
               (center_x + 1, center_y - 1),
               (center_x - 1, center_y + 1),
               (center_x + 1, center_y + 1)]:
        if is_tile_walkable(xy[0], xy[1], None):
            free_tiles.append((xy[0] - center_x, xy[1] - center_y))
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
        if sprite.target:
            id_to_remove = sprite.attack_sprite()
            if id_to_remove:
                ids_to_remove.append(id_to_remove)
    for sprite_id in ids_to_remove:
        del (Sprite.sprites[sprite_id])


def get_sprites_around_xy(x_range, y_range):
    sprites_in_range = {}
    for sprite_id, sprite in Sprite.sprites.items():
        if sprite.x in x_range and sprite.y in y_range:
            sprites_in_range[sprite_id] = sprite
    return sprites_in_range


def get_items_around_xy(x_range, y_range):
    items_in_range = {}
    for item_id, item in Item.items.items():
        if item.x in x_range and item.y in y_range:
            items_in_range[item_id] = item
    return items_in_range


id_counter = 1
player1 = Player.Player(id_counter, "Rob", 45, 9)
id_counter += 1
# Creates 15 randomly places enemies.

# e = Enemy.Enemy(id_counter, 46, 9, "giant_eye")
for i in range(10):
    x, y = random.randint(0, 80), random.randint(0, 20)
    while not is_tile_walkable(x, y, None):
        x, y = random.randint(0, 80), random.randint(0, 20)
    Enemy.Enemy(id_counter, x, y, "giant_eye")
    id_counter += 1

for i in range(10):
    x, y = random.randint(0, 80), random.randint(0, 20)
    while not is_tile_walkable(x, y, None):
        x, y = random.randint(0, 80), random.randint(0, 20)
    Enemy.Enemy(id_counter, x, y, "grey_rat")
    id_counter += 1

# hk = Item.HealthKit(id_counter, 47, 9)
for i in range(10):
    x, y = random.randint(0, 80), random.randint(0, 20)
    while not is_tile_walkable(x, y, None):
        x, y = random.randint(0, 80), random.randint(0, 20)
    Item.HealthKit(id_counter, x, y)
    id_counter += 1
