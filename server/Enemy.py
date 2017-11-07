import configuration as conf
import server.Sprite as Sprite
import pygame as pg

enemy_types = {
    "giant_eye": {
        "max_health": 100,
        "attack": 5,
        "attack_speed": 1,
        "speed": 1.2,
        "name": "Giant Eye",
        "img": "graphics/crawl-tiles Oct-5-2010/dc-mon/giant_eyeball.png",
        "exp_to_gain": 5,
        "range": 1
    },
    "grey_rat": {
        "max_health": 50,
        "attack": 3,
        "attack_speed": 2,
        "speed": 5,
        "name": "Rat",
        "img": "graphics/crawl-tiles Oct-5-2010/dc-mon/animals/grey_rat.png",
        "exp_to_gain": 2,
        "range": 1
    }
}


class Enemy(Sprite.Sprite):
    def __init__(self, enemy_id, starting_x, starting_y, enemy_type):
        super(Enemy, self).__init__(enemy_id, starting_x, starting_y)
        self.enemy_type = enemy_type
        self.max_health = enemy_types[self.enemy_type]["max_health"]
        self.health = self.max_health
        self.attack = enemy_types[self.enemy_type]["attack"]
        self.attack_speed = enemy_types[self.enemy_type]["attack_speed"]
        self.range = enemy_types[self.enemy_type]["range"]
        self.map_level = 0
        self.sprite_type = "Enemy"
        raw_image = pg.image.load(enemy_types[self.enemy_type]["img"])
        self.base_image = pg.transform.scale(raw_image, (conf.GRID_SQUARE_SIZE, conf.GRID_SQUARE_SIZE))
        self.base_image_flipped = pg.transform.flip(self.base_image, True, False)
        self.images = [self.base_image]
        self.name = enemy_types[self.enemy_type]["name"]
        self.speed = enemy_types[self.enemy_type]["speed"]
        self.target = 1
        Sprite.sprites[self.sprite_id] = self
