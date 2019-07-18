import numpy as np


def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_direction(pos1, pos2):
    dir = (pos2[0] - pos1[0], pos2[1] - pos1[1])
    dir = (int(dir[0]/abs(dir[0])), 0) if abs(dir[0]) > abs(dir[1]) else \
        (0, int(dir[1]/abs(dir[1])))
    return dir


def next_move(pos, board):
    moves = {
        "RIGHT": np.array((0, 1)),
        "UP": np.array((-1, 0)),
        "LEFT": np.array((0, -1)),
        "DOWN": np.array((1, 0)),
    }
    if "b" not in board:
        return "CLEAN"
    dirt = np.argwhere(board == "d")
    dirt = [tuple(pos) for pos in dirt]
    bot = np.argwhere(board == "b")[0]
    closest = None
    for pos in dirt:
        if not closest or dist(bot, pos) < closest[0]:
            closest = [dist(bot, pos), pos]
    direction = get_direction(bot, closest[1])
    for dir, pair in moves.items():
        if np.array_equal(direction, pair):
            return dir
