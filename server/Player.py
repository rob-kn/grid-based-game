import configuration as conf
from server.Sprite import Sprite


class Player(Sprite):
    def __init__(self, player_id, player_name, starting_x, starting_y):
        super(Player, self).__init__(player_id, starting_x, starting_y)
        self.name = player_name
        self.max_health = 100
        self.health = 40
        self.mana = 20
        self.max_mana = 20
        self.speed = 5  # 8=8 frames per tile, 4=16f/t, 2=32f/t, 1=64f/t
        self.attack = 20
        self.attack_speed = 1
        self.range = 1
        self.sprite_type = "Player"
        self.images = [conf.player_img, conf.player_legs, conf.player_body]

