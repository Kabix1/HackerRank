BOT = "b"
EMPTY = "-"
DIRT = "d"

A = 0.2455475233408131
B = 0.15227
C = 3.981984996122549
D = 0
CLUSTER_LENGTH = 3
DISTANCES_CONSIDERED = 4


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


def get_dirt_at_distance(pos, board, n):
    dirts = []
    start = [pos[0] + n, pos[1]]
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
    for n in range(1, max_distance + 1):
        dirts = get_dirt_at_distance(pos, board, n)
        if dirts:
            return dirts


def dirt_score(pos, dirt, board, shape):
    max_pos = (shape[0] / 2)**2 + (shape[1] / 2)**2
    cluster_score, pos_score = 0, 0
    distance_score = dist(pos, dirt) / (shape[0] + shape[1])
    adj_pos = (dirt[0] - shape[0] / 2, dirt[1] - shape[1] / 2)
    pos_score = (adj_pos[0]**2 + adj_pos[1]**2) / max_pos
    n_dirt, n_squares = 0, 0
    for d in range(1, CLUSTER_LENGTH + 1):
        n_dirt += len(get_dirt_at_distance(dirt, board, d))
        n_squares += 4 * d
    cluster_score = n_dirt / n_squares
    return -cluster_score + A * pos_score + B * pos_score**2 - C * distance_score - D * distance_score**2


def next_move(pos, board):
    shape = (len(board), len(board[0]))
    if board[pos[0]][pos[1]] == DIRT:
        return "CLEAN"
    dirts = find_closest_dirts(pos, board)
    d = dist(pos, dirts[0])
    for i in range(d, d + DISTANCES_CONSIDERED + 1):
        dirts.extend(get_dirt_at_distance(pos, board, i))
        dirts.extend(get_dirt_at_distance(pos, board, i))
    best_dirt = None
    best_score = -999999999
    for dirt in dirts:
        if dirt_score(pos, dirt, board, shape) > best_score:
            best_dirt = dirt
            best_score = dirt_score(pos, dirt, board, shape)

    vector = [best_dirt[0] - pos[0], best_dirt[1] - pos[1]]
    dir = ""
    if vector[0]:
        dir = "DOWN" if vector[0] > 0 else "UP"
    else:
        dir = "RIGHT" if vector[1] > 0 else "LEFT"
    return dir
