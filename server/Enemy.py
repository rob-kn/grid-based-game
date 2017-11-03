import configuration as conf
from server.Sprite import Sprite


enemy_types = {"giant_eye": {"max_health": 100,
                             "attack": 20,
                             "speed": 3.5,
                             "name": "Giant Eye",
                             "img": conf.giant_eye_img}}
enemies = []


class Enemy(Sprite):
    def __init__(self, enemy_id, starting_x, starting_y, enemy_type):
        self.max_health = 100
        self.health = 100
        self.speed = 3.5
        self.attack = 5
        self.map_level = 0
        self.sprite_type = "Enemy"
        self.enemy_type = enemy_type
        self.image = enemy_types[self.enemy_type]["img"]
        self.name = enemy_types[self.enemy_type]["name"]
        enemies.append(self)
        super(Enemy, self).__init__(enemy_id, starting_x, starting_y)

