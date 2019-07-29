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


def get_dirt_at_distance(pos, board, dist):
    dirts = []
    start = [pos[0] + dist, pos[1]]
    curr = list(start)
    dx, dy = -1, 1
    while True:
        if is_dirt(curr, board):
            dirts.append(tuple(curr))
        curr[0] += dx
        curr[1] += dy
        if curr[0] == pos[0]:
            dy = -dy
        if curr[1] == pos[1]:
            dx = -dx
        if curr == start:
            return dirts


def find_closest_dirts(pos, board, max_distance=0):
    if not max_distance:
        max_distance = len(board) + len(board[0])
    n_moves = 1
    start = (pos[0] + n_moves, pos[1])
    curr = list(start)
    dx, dy = -1, 1
    dirts = []
    for n in range(1, max_distance + 1):
        dirts = get_dirt_at_distance(pos, board, n)
        if dirts:
            return dirts


def dirt_score(dirt, board, shape):
    adj_pos = (dirt[0] - shape[0] / 2, dirt[1] - shape[1] / 2)
    pos_score = adj_pos[0]**2 + adj_pos[1]**2
    if not pos_score:
        pos_score = 1
    else:
        pos_score = 1 / pos_score
    close_dirt = []
    close_dirt.extend(get_dirt_at_distance(dirt, board, 1))
    close_dirt.extend(get_dirt_at_distance(dirt, board, 2))
    close_dirt.extend(get_dirt_at_distance(dirt, board, 3))
    if close_dirt:
        return len(close_dirt) * pos_score
    return pos_score


def _next_move(pos, board):
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
