# This simulates the server side of storing the player information.
# players_info stores:
# grid_pos - a position for the player in the grid
# moving offset - offset that player has moved so far
players_info = {1: {
    "grid_pos": (14, 14),
    "moving_offset": (0, 0)
}
}


def get_player_grid_pos(player_id):
    return players_info[player_id]["grid_pos"]


def set_player_grid_pos(player_id, new_xy):
    players_info[player_id]["grid_pos"] = new_xy


def get_player_moving_offset(player_id):
    return players_info[player_id]["moving_offset"]


def set_player_moving_offset(player_id, new_offset):
    players_info[player_id]["moving_offset"] = new_offset
