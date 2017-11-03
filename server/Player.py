import configuration as conf
import math
from server.Sprite import Sprite
#
# sorted(lst, key=lambda i: (i.x, i.y))


class Player(Sprite):
    def __init__(self, player_id, player_name, starting_x, starting_y):
        self.name = player_name
        self.max_health = 100
        self.health = 100
        self.speed = 5 # 8=8 frames per tile, 4=16f/t, 2=32f/t, 1=64f/t
        self.attack = 5
        self.sprite_type = "Player"
        self.target = 7
        self.image = conf.player_img
        super(Player, self).__init__(player_id, starting_x, starting_y)
