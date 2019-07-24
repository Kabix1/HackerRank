#!/usr/bin/env python

# import main
import numpy as np
import sys
import random
import Strategies
import pprint

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

SHAPE = (9, 30)


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
    # board = np.random.choice([EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, DIRT],
    board = np.random.choice([EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, DIRT],
                             size=SHAPE)
    bot_pos = tuple(np.random.randint(0, min(SHAPE), size=(2)))
    if board[bot_pos] == EMPTY:
        board[bot_pos] = BOT
    return (bot_pos, board)


def test_all():
    modules = [module for module in dir(Strategies) if "__" not in module]
    modules = [getattr(Strategies, module) for module in modules]
    strats = [module for module in modules if hasattr(module, "next_move")]
    num_tries = 1000
    num_moves = {strat.__name__: [] for strat in strats}
    for _ in range(num_tries):
        pos, board = generate_board()
        diff = 0
        for strat in strats:
            num_moves[strat.__name__].append(try_strategy(strat, pos, board))
            if not diff:
                diff = num_moves[strat.__name__][-1]
            else:
                diff -= num_moves[strat.__name__][-1]
                if diff >= 35:
                    print(board)
    width = max([len(name) for name in num_moves.keys()])
    mov = list(num_moves.values())
    diffs = [mov[1][i] - mov[0][i] for i in range(num_tries)]
    avg = sum(diffs) / num_tries
    std = (sum(map(lambda x: (x - avg)**2, diffs)) / num_tries)**0.5
    diffs.sort()
    print(diffs)
    print(f"diffs{' ':<{width-5}}  {avg} +- {std/(num_tries**0.5):.3}")
    for strat, moves in num_moves.items():
        avg = sum(moves) / num_tries
        std = (sum(map(lambda x: (x - avg)**2, moves)) / num_tries)**0.5
        print(f"{strat:<{width}}  {avg} +- {std/(num_tries**0.5):.3}")


def try_strategy(strat, orig_pos, orig_board):
    count = 0
    board = np.array(orig_board)
    pos = tuple(orig_pos)
    while not is_done(board):
        # print("#" * len(board[0]))
        # for row in board:
        #     print("".join(row))
        # print("#" * len(board[0]))
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
    return count
    # print(f"Success! Did it in {count} moves [{strat.__name__}]")
