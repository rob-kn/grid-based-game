import configuration as conf
import server.Sprite as Sprite
import server.Enemy as Enemy
from time import time


level_boundaries = {
    1: 0,
    2: 15,
    3: 50,
    4: 100,
    5: 175
}


class Player(Sprite.Sprite):
    def __init__(self, player_id, player_name, starting_x, starting_y):
        super(Player, self).__init__(player_id, starting_x, starting_y)
        self.name = player_name
        self.max_health = 100
        self.health = 100
        self.mana = 20
        self.max_mana = 20
        self.speed = 5  # 8=8 frames per tile, 4=16f/t, 2=32f/t, 1=64f/t
        self.attack = 40
        self.attack_speed = 1
        self.range = 1
        self.sprite_type = "Player"
        self.player_level = 1
        self.last_level_up_time = 0
        self.exp = 0
        #self.images = [conf.player_img, conf.player_legs, conf.player_body]
        self.images = [conf.deep_troll]
        Sprite.sprites[self.sprite_id] = self

    def add_experience(self, enemy_type):
        exp_to_add = Enemy.enemy_types[enemy_type]["exp_to_gain"]
        self.exp += exp_to_add
        exp_req_for_levelup = level_boundaries[self.player_level + 1]
        if self.exp >= exp_req_for_levelup:
            self.player_level += 1
            self.last_level_up_time = time()
            print("Leveled up! Now level {}.".format(self.player_level))
