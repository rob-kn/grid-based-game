import configuration as conf

enemy_types = {"giant_eye": {"max_health": 100,
                             "attack": 20,
                             "speed": 5,
                             "img": conf.giant_eye_img}}
enemies = []


class Enemy:
    def __init__(self, starting_x, starting_y, type):
        self.health = 100
        self.attack = 5
        self.speed = 1
        self.offset = (0, 0)
        self.x = starting_x
        self.y = starting_y
        self.map_level = 0
        self.image = enemy_types[type]["img"]
        enemies.append(self)

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
        # TODO: Currently player will move slower is grid blocks are bigger (needs adjusting to variables)
        current_offset_x, current_offset_y = self.offset
        if -self.speed < current_offset_x < self.speed and -self.speed < current_offset_y < self.speed:
            current_offset_x, current_offset_y = 0, 0
        if current_offset_x > 0:
            current_offset_x -= self.speed
        elif current_offset_x < 0:
            current_offset_x += self.speed
        if current_offset_y > 0:
            current_offset_y -= self.speed
        elif current_offset_y < 0:
            current_offset_y += self.speed
        self.offset = (current_offset_x, current_offset_y)