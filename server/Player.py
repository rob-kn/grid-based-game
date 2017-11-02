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
