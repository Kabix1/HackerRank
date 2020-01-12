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
# The output is the action that is taken by the bot in the current step, and it can be either one of the tests in 4 directions or cleaning up the cell in which it is currently located. The valid output strings are LEFT, RIGHT, UP and DOWN or CLEAN. If the bot ever reaches a dirty cell, output CLEAN to clean the dirty cell. Repeat this process until all the cells on the grid are cleaned.
#########################################################################################################

import random
import numpy as np


def next_move(board):
    x_bot = -1
    dirs = ["UP", "LEFT", "DOWN", "RIGHT"]
    bot_pos = np.where(board == "b")
    if bot_pos[0].size == 0:
        return "CLEAN"
    # for y, row in enumerate(board):
    #     if row.count("b") >= 1:
    #         x_bot = row.index("b")
    #         # y_bot = y
    return "DOWN"
    # else:
        # print(dirs[random.randint(0, 3)])


def is_dirty(board):
    for row in board:
        if "d" in row:
            return True
    return False


def make_move(bot_pos, board, move):
    if move == "CLEAN":
        if board[bot_pos] == "d":
            board[bot_pos] = "b"
        return bot_pos
    new_pos = list(bot_pos)
    if board[bot_pos] == "b":
        board[bot_pos] = "-"
    if move == "RIGHT":
        new_pos[1] += 1
    elif move == "UP":
        new_pos[0] -= 1
    elif move == "LEFT":
        new_pos[1] -= 1
    elif move == "DOWN":
        new_pos[0] += 1
    bot_pos = tuple(new_pos)
    if max(bot_pos) > 2 or min(bot_pos) < 0:
        return False
    elif board[bot_pos] == "-":
        print(board[tuple(bot_pos)])
        board[bot_pos] = "b"
    return bot_pos

def test_case():
    initial_board = np.array([["-", "-", "b"],
                              ["-", "-", "d"],
                              ["d", "-", "-"]])
    board = initial_board
    bot_pos = (0, 2)
    while is_dirty(board):
        move = next_move(board)
        print(move)
        print(board)
        bot_pos = make_move(bot_pos, board, move)
        if not bot_pos:
            break
        # print(bot_pos)
        # print(board)
        # print(np.where(board == "b"))
        # if move == "CLEAN" and board[bot_pos] == "d":
            # print("hej")
    else:
        print("Clean!")
    # next_move([["-", "-", "b"], ["-", "-", "-"], ["-", "-", "-"]])



def main():
    test_case()


if __name__ == "__main__":
    main()
    # next_move([["-", "-", "b"], ["-", "-", "-"], ["-", "-", "-"]])
