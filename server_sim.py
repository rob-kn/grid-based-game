# This simulates the server side of storing the player information.
# players_info stores:
# grid_pos - a position for the player in the grid
# moving offset - offset that player has moved so far
import configuration as conf


class Player:
    def __init__(self, player_id, starting_x, starting_y):
        self.player_id = player_id
        self.health = 100
        self.attack = 5
        self.speed = 1
        self.offset = (0, 0)
        self.x = starting_x
        self.y = starting_y
        self.map_level = 0

    def reset_offset(self, new_grid_pos, old_grid_pos):
        new_offset_x = 0
        new_offset_y = 0
        new_offset_x = -conf.GRID_SQUARE_SIZE if new_grid_pos[0] < old_grid_pos[0] else new_offset_x
        new_offset_x = +conf.GRID_SQUARE_SIZE if new_grid_pos[0] > old_grid_pos[0] else new_offset_x
        new_offset_y = -conf.GRID_SQUARE_SIZE if new_grid_pos[1] < old_grid_pos[1] else new_offset_y
        new_offset_y = +conf.GRID_SQUARE_SIZE if new_grid_pos[1] > old_grid_pos[1] else new_offset_y
        self.offset = (new_offset_x, new_offset_y)

    def reduce_offset(self):
        # gets current offset and converges it to zero.
        # TODO: Offsets can be stored locally (not from server)
        # TODO: Currently player will move slower is grid blocks are bigger (needs adjusting to variables)
        current_offset_x, current_offset_y = self.offset
        if -4 < current_offset_x < 4 and -4 < current_offset_y < 4:
            current_offset_x, current_offset_y = 0, 0
        if current_offset_x > 0:
            current_offset_x -= 4
        elif current_offset_x < 0:
            current_offset_x += 4
        if current_offset_y > 0:
            current_offset_y -= 4
        elif current_offset_y < 0:
            current_offset_y += 4
        self.offset = (current_offset_x, current_offset_y)


class Enemy:
    def __init__(self, enemy_type, starting_x, starting_y):
        self.enemy_type = enemy_type
        self.health = enemy_types[enemy_type]["max_health"]
        self.attack = enemy_types[enemy_type]["attack"]
        self.offset = (0, 0)
        self.x = starting_x
        self.y = starting_y
        enemies.append(self)

    def update(self):
        pass


players_info = {1: {
    "grid_pos": (45, 9),
    "moving_offset": (0, 0)
}
}
enemies = []
enemy_types = {"giant_eye": {"max_health": 100,
                             "attack": 20,
                             "speed": 5}}

player1 = Player(1, 45, 9)


def get_player():
    return player1


def set_player(p):
    global player1
    player1 = p
