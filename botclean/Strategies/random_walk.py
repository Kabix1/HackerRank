import numpy as np
import random


def is_valid(pos, board):
    try:
        board[pos]
    except IndexError:
        return False
    if min(pos) < 0:
        return False
    return True


def next_move(pos, board):
    moves = {
        "RIGHT": np.array((0, 1)),
        "UP": np.array((-1, 0)),
        "LEFT": np.array((0, -1)),
        "DOWN": np.array((1, 0)),
    }
    dirs = ["UP", "LEFT", "DOWN", "RIGHT"]
    if "b" not in board:
        return "CLEAN"
    new_pos = (-1, -1)
    while not is_valid(new_pos, board):
        dir = dirs[random.randint(0, 3)]
        new_pos = tuple(pos + moves[dir])
    return dir
