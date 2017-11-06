import configuration as conf
from server.Sprite import Sprite

enemy_types = {"giant_eye": {"max_health": 100,
                             "attack": 5,
                             "attack_speed": 2,
                             "speed": 1.2,
                             "name": "Giant Eye",
                             "img": conf.giant_eye_img,
                             "range": 1}}
enemies = []


class Enemy(Sprite):
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
        self.images = [enemy_types[self.enemy_type]["img"]]
        self.name = enemy_types[self.enemy_type]["name"]
        self.speed = enemy_types[self.enemy_type]["speed"]
        self.target = 1
        enemies.append(self)

