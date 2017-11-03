import configuration as conf

sprites = []


class Sprite:
    def __init__(self, sprite_id, starting_x, starting_y):
        self.sprite_id = sprite_id
        self.offset = (0, 0)
        self.offset_float = (0.0, 0.0)
        self.x = starting_x
        self.y = starting_y
        self.map_level = 0
        sprites.append(self)

    def reset_offset(self, new_grid_pos, old_grid_pos):
        """Sets the appropriate offset when given an updated position in the grid."""
        new_offset_x = 0
        new_offset_y = 0
        new_offset_x = -conf.GRID_SQUARE_SIZE if new_grid_pos[0] < old_grid_pos[0] else new_offset_x
        new_offset_x = +conf.GRID_SQUARE_SIZE if new_grid_pos[0] > old_grid_pos[0] else new_offset_x
        new_offset_y = -conf.GRID_SQUARE_SIZE if new_grid_pos[1] < old_grid_pos[1] else new_offset_y
        new_offset_y = +conf.GRID_SQUARE_SIZE if new_grid_pos[1] > old_grid_pos[1] else new_offset_y
        self.offset = (new_offset_x, new_offset_y)
        self.offset_float = (float(new_offset_x), float(new_offset_y))

    def reduce_offset(self):
        """
        Converges current offset to zero. Updates a float version to allow for varying speeds.
        If the movement is diagonal, the player moves twice as slow.
        """
        current_offset_x, current_offset_y = self.offset_float
        if -self.speed < current_offset_x < self.speed and -self.speed < current_offset_y < self.speed:
            current_offset_x, current_offset_y = 0.0, 0.0
        change_x, change_y = 0.0, 0.0
        if current_offset_x > 0:
            change_x -= self.speed
        elif current_offset_x < 0:
            change_x += self.speed
        if current_offset_y > 0:
            change_y -= self.speed
        elif current_offset_y < 0:
            change_y += self.speed
        if change_x and change_y:
            change_x /= 2
            change_y /= 2
        self.offset = (int(current_offset_x + change_x), int(current_offset_y + change_y))
        self.offset_float = (current_offset_x + change_x, current_offset_y + change_y)


