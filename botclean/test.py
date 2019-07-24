#!/usr/bin/env python

# import main
import numpy as np
import sys
import random
import Strategies

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


def generate_board():
    num_cells = 25
    board_num = [random.randint(0, 1) for _ in range(num_cells)]
    board = [DIRT if n else EMPTY for n in board_num]
    board = np.array(board).reshape((5, 5))
    bot_pos = tuple(np.random.randint(0, 5, size=(2)))
    if board[bot_pos] == EMPTY:
        board[bot_pos] = BOT
    return (bot_pos, board)


def test_all():
    modules = [module for module in dir(Strategies) if "__" not in module]
    modules = [getattr(Strategies, module) for module in modules]
    strats = [module for module in modules if hasattr(module, "next_move")]
    for strat in strats:
        try_strategy(strat)


def try_strategy(strat):
    num_tries = 25
    count = 0
    for _ in range(num_tries):
        pos, board = generate_board()
        while not is_done(board):
            move = strat.next_move(pos, board.tolist())
            new_pos = update_pos(pos, move)
            if not is_valid(new_pos, board):
                print(
                    f"Board: {board} tried to move {move} from {pos} [{strat.__name__}]"
                )
                sys.exit(1)
            update_board(pos, new_pos, board)
            pos = new_pos
            count += 1
            assert count < 5000
    print(f"Success! Did it in {count/num_tries} moves [{strat.__name__}]")
