BOT = "b"
EMPTY = "-"
DIRT = "d"


def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def is_dirt(pos, board):
    if min(pos) < 0:
        return False
    if pos[0] >= len(board):
        return False
    if pos[1] >= len(board[0]):
        return False
    if board[pos[0]][pos[1]] != DIRT:
        return False
    return True


def find_closest_dirts(pos, board, max_distance=0):
    if not max_distance:
        max_distance = len(board) + len(board[0])
    n_moves = 1
    start = (pos[0] + n_moves, pos[1])
    curr = list(start)
    dx, dy = -1, 1
    dirts = []
    while n_moves <= max_distance:
        if is_dirt(curr, board):
            # if not best_dirt or best_dirt[1] > dirt_score(curr):
            dirts.append(tuple(curr))
        curr[0] += dx
        curr[1] += dy
        if curr[0] == pos[0]:
            dy = -dy
        if curr[1] == pos[1]:
            dx = -dx
        if curr == list(start):
            if dirts:
                return dirts
            # if best_dirt:
            # return best_dirt[0]
            n_moves += 1
            start = (pos[0] + n_moves, pos[1])
            curr = list(start)


def dirt_score(dirt, board, shape):
    close_dirt = find_closest_dirts(dirt, board, max_distance=2)
    if close_dirt:
        return len(close_dirt)
    return 0
    # return len(find_closest_dirts(dirt, board, max_distance=1))


def next_move(pos, board):
    # x_score = abs(dirt[0] - shape[0] // 2)
    # y_score = abs(dirt[1] - shape[1] // 2)
    # return x_score**2 + y_score**2

    shape = (len(board), len(board[0]))
    if board[pos[0]][pos[1]] == DIRT:
        return "CLEAN"
    closest = find_closest_dirts(pos, board)
    best_dirt = None
    best_score = 0
    for dirt in closest:
        if not best_dirt or dirt_score(dirt, board, shape) < best_score:
            best_dirt = dirt
            best_score = dirt_score(dirt, board, shape)

    vector = [best_dirt[0] - pos[0], best_dirt[1] - pos[1]]
    dir = ""
    if vector[0]:
        dir = "DOWN" if vector[0] > 0 else "UP"
    else:
        dir = "RIGHT" if vector[1] > 0 else "LEFT"
    return dir
