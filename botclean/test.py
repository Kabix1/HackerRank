#!/usr/bin/env python

import main
import numpy as np
import sys

MOVES = {
    "RIGHT": np.array((0, 1)),
    "UP": np.array((-1, 0)),
    "LEFT": np.array((0, -1)),
    "DOWN": np.array((1, 0)),
    "CLEAN": np.array((0, 0))
}

BOT = "b"
EMPTY = "-"
DIRT = "d"


def is_done(board):
    return DIRT not in board


def is_valid(pos, board):
    try:
        board[pos]
    except IndexError:
        return False
    if min(pos) < 0:
        return False
    return True


def update_pos(pos, move):
    if move not in MOVES:
        print(f"{move} not a valid move")
        sys.exit(1)
    change = MOVES[move]
    return tuple(pos + change)


def update_board(old_pos, new_pos, board):
    if old_pos == new_pos:  # Bot is cleaning
        board[new_pos] = BOT
        return
    if BOT in board:
        board[old_pos] = EMPTY
    if board[new_pos] == EMPTY:
        board[new_pos] = BOT


def test1():
    board = np.array([[DIRT, EMPTY, BOT], [EMPTY, EMPTY, DIRT],
                      [DIRT, DIRT, EMPTY]])
    pos = (0, 2)
    count = 0
    while not is_done(board):
        move = main.next_move(board)
        new_pos = update_pos(pos, move)
        if not is_valid(new_pos, board):
            print(f"Board: {board} tried to move {move} from {pos}")
            sys.exit(1)
        update_board(pos, new_pos, board)
        pos = new_pos
        count += 1
        assert count < 500
    print(f"Success! Did it in {count} moves")
