# This simulates the server side of storing the player information.

#pos = (50, 50)
#grid_pos = (1, 1)
players_info = {1: {
                    "moving_pos": (50, 50),
                    "grid_pos": (1, 1)
                    }
                }


def get_player_moving_pos(player_id):
    return players_info[player_id]["moving_pos"]


def set_player_moving_pos(player_id, new_xy):
    players_info[player_id]["moving_pos"] = new_xy


def get_player_grid_pos(player_id):
    return players_info[player_id]["grid_pos"]


def set_player_grid_pos(player_id, new_xy):
    players_info[player_id]["grid_pos"] = new_xy
