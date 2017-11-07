import configuration as conf
import server.Sprite as Sprite

enemy_types = {
    "giant_eye": {
        "max_health": 100,
        "attack": 5,
        "attack_speed": 1,
        "speed": 1.2,
        "name": "Giant Eye",
        "img": conf.giant_eye_img,
        "exp_to_gain": 5,
        "range": 1
    },
    "grey_rat": {
        "max_health": 50,
        "attack": 3,
        "attack_speed": 2,
        "speed": 5,
        "name": "Rat",
        "img": conf.grey_rat_img,
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
        self.images = [enemy_types[self.enemy_type]["img"]]
        self.name = enemy_types[self.enemy_type]["name"]
        self.speed = enemy_types[self.enemy_type]["speed"]
        self.target = 1
        Sprite.sprites[self.sprite_id] = self
