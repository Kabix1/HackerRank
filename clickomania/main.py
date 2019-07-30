import numpy as np

COLORS = ['V', 'I', 'B', 'G', 'Y', 'O', 'R']
EMPTY = "-"
DIRS = np.array([(1, 0), (0, -1), (-1, 0), (0, 1)])
RIGHTMOST = -1


def print_board(board):
    print("#" * (board.shape[0] + 2))
    for row in board:
        s = "".join(row)
        print(f"#{s}#")
    print("#" * (board.shape[0] + 2))


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


def remove_group(board, x, y):
    color = board[x][y]
    group = [(x, y)]
    board[(x, y)] = EMPTY
    for pos in group:
        for d in DIRS:
            pos2 = tuple(pos + d)
            if is_color(board, pos2, color):
                group.append(pos2)
                board[pos2] = EMPTY
    # print(group)


def generate_board(x: int, y: int, k: int) -> list:
    colors = COLORS[:k]
    board = np.random.choice(colors, size=(x, y))
    return board


def rule1(board):
    for column in board.T:
        scol = "".join(column)
        scol = f'{scol.replace(EMPTY, ""):->{board.shape[1]}}'
        column[:] = np.array(list(scol))


def rule2(board):
    global RIGHTMOST
    empty = [EMPTY] * board.shape[1]
    empty_columns = []
    for i, column in enumerate(board.T[:RIGHTMOST]):
        if list(column) == empty:
            # board[:, i:] = np.hstack(
            #     (board[:, i + 1:], np.array([[EMPTY] * board.shape[1]]).T))
            # RIGHTMOST -= 1
            empty_columns.append(i)
    for c in empty_columns[-1::-1]:
        cols = np.hstack(
            (board[:, c + 1:], np.array([[EMPTY] * board.shape[1]]).T))
        board[:, c:] = cols
    RIGHTMOST -= len(empty_columns)


if __name__ == "__main__":
    x, y, k = 5, 5, 2
    board = generate_board(x, y, k)
    RIGHTMOST = x - 1
    for _ in range(3):
        print_board(board)
        remove_group(board, y - 1, 0)
        rule1(board)
        rule2(board)
