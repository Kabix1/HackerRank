# COLORS = ['V', 'I', 'B', 'G', 'Y', 'O', 'R']
EMPTY = "-"
# DIRS = np.array([(1, 0), (0, -1), (-1, 0), (0, 1)])
RIGHTMOST = -1


def is_color(board, x, y, color):
    if min(x, y) < 0:
        return False
    if x >= len(board):
        return False
    if y >= len(board[0]):
        return False
    if board[x][y] != color:
        return False
    return True


def get_group(board, x, y):
    color = board[x][y]
    group = []
    if color == EMPTY:
        return []
    test = [(x, y)]
    for i, j in test:
        if is_color(board, i, j, color):
            group.append((i, j))
            board[i][j] = EMPTY
            test.append((i + 1, j))
            test.append((i, j - 1))
            test.append((i - 1, j))
            test.append((i, j + 1))
    if len(group) > 1:
        return (group, color)
    return []


def get_groups(board):
    copy = [row.copy() for row in board]
    groups = []
    x_max, y_max = len(copy), len(copy[0])
    for x in range(x_max):
        for y in range(y_max):
            group = get_group(copy, x, y)
            if group:
                groups.append(group)
    return groups


def get_color_count(board):
    color_count = {}
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] not in color_count:
                color_count[board[x][y]] = 1
            else:
                color_count[board[x][y]] += 1
    return color_count


def next_move(x, y, board):
    groups = get_groups(board)
    groups.sort(key=lambda x: len(x[0]))
    return groups[0][0][0]
    # print(groups)
    # color_count = get_color_count(board)
    # for group, color in groups:
    #     if color_count[color] - len(group) == 0:
    #         return group[0]
    # for group, color in groups:
    # if color_count[color] - len(group) != 1:
    # return group[0]
    # return groups[0][0][0]
