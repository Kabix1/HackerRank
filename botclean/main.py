#!/usr/bin/env python
########################################################################################################
# Input Format
#
# The first line contains two space separated integers which indicate the current pos of the bot.
# The board is indexed using Matrix Convention
# 5 lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters: 'b' (ascii value 98) indicates the bot's current pos, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid.
#
# Note If the bot is on a dirty cell, the cell will still have 'd' on it.
#
# Output Format
#
# The output is the action that is taken by the bot in the current step, and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.
#########################################################################################################

import random
import numpy as np

ROUTE = []


class Node:
    def __init__(self, pos):
        self.neighbours = []
        self.pos = pos

    def calc_dist(self, pos):
        return abs(pos[0] - self.pos[0]) + abs(pos[1] - self.pos[1])

    def add_neighbour(self, cell):
        dist = self.calc_dist(cell.pos)
        self.neighbours.append({"cell": cell, "dist": dist})


def is_valid(pos, board):
    try:
        board[pos]
    except IndexError:
        return False
    if min(pos) < 0:
        return False
    return True


# def dyn_solve(start, board):

# def dyn_next_move(pos, board):
#     global ROUTE
#     if not ROUTE:
#         ROUTE = dyn_solve(pos, board)
#     if "b" not in board:
#         return "CLEAN"
#     return ROUTE.pop()


def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_directions(pos1, pos2):
    return (pos2[0] - pos1[0], pos2[1] - pos1[1])


def toward_closest(pos, board):
    if "b" not in board:
        return "CLEAN"
    dirt = np.argwhere(board == "d")
    dirt = [tuple(pos) for pos in dirt]
    bot = np.argwhere(board == "b")[0]
    closest = None
    for pos in dirt:
        if not closest or dist(bot, pos) < closest[0]:
            closest = [dist(bot, pos), pos]


def random_walk(pos, board):
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


def next_move(pos, board):
    board = np.array(board)
    toward_closest(pos, board)
    return 0
    dirt = np.argwhere(board == "d")
    bot = np.argwhere(board == "b")
    positions = np.concatenate((bot, dirt))
    positions = [tuple(pos) for pos in positions]
    nodes = [Node(pos) for pos in positions]


if __name__ == "__main__":
    next_move((0, 2), [["-", "d", "b"], ["-", "d", "-"], ["d", "-", "d"]])
