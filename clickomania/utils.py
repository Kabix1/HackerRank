import numpy as np

COLORS = ['V', 'I', 'B', 'G', 'Y', 'O', 'R']
EMPTY = "-"
DIRS = np.array([(1, 0), (0, -1), (-1, 0), (0, 1)])
RIGHTMOST = -1


def is_color(board, pos, color):
    if min(pos) < 0:
        return False
    if pos[0] >= board.shape[0]:
        return False
    if pos[1] >= board.shape[1]:
        return False
    if board[pos] != color:
        return False
    return True


def get_group(board, pos):
    color = board[pos]
    assert color != EMPTY
    group = [pos]
    board_copy = board.copy()
    board_copy[pos] = EMPTY
    for pos in group:
        for d in DIRS:
            pos2 = tuple(pos + d)
            if is_color(board_copy, pos2, color):
                group.append(pos2)
                board_copy[pos2] = EMPTY
    assert len(group) > 1
    return group
