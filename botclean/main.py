#!/usr/bin/env python
########################################################################################################
# Input Format
#
# The first line contains two space separated integers which indicate the current position of the bot.
# The board is indexed using Matrix Convention
# 5 lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters: 'b' (ascii value 98) indicates the bot's current position, 'd' (ascii value 100) indicates a dirty cell and '-' (ascii value 45) indicates a clean cell in the grid.
#
# Note If the bot is on a dirty cell, the cell will still have 'd' on it.
#
# Output Format
#
# The output is the action that is taken by the bot in the current step, and it can be either one of the movements in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.
#########################################################################################################

import random


def next_move(board):
    # x_bot, y_bot = -1, -1
    x_bot = -1
    dirs = ["UP", "LEFT", "DOWN", "RIGHT"]
    if "b" not in board:
        return "CLEAN"
    else:
        return dirs[random.randint(0, 3)]


if __name__ == "__main__":
    next_move([["-", "-", "b"], ["-", "-", "-"], ["-", "-", "-"]])
