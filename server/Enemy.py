import configuration as conf
from server.Sprite import Sprite


enemy_types = {"giant_eye": {"max_health": 100,
                             "attack": 20,
                             "speed": 1.5,
                             "name": "Giant Eye",
                             "img": conf.giant_eye_img,
                             "range": 0}}
enemies = []


class Enemy(Sprite):
    def __init__(self, enemy_id, starting_x, starting_y, enemy_type):
        self.enemy_type = enemy_type
        self.max_health = enemy_types[self.enemy_type]["max_health"]
        self.health = self.max_health
        self.attack = enemy_types[self.enemy_type]["attack"]
        self.map_level = 0
        self.sprite_type = "Enemy"
        self.image = enemy_types[self.enemy_type]["img"]
        self.name = enemy_types[self.enemy_type]["name"]
        self.speed = enemy_types[self.enemy_type]["speed"]
        enemies.append(self)
        super(Enemy, self).__init__(enemy_id, starting_x, starting_y)

