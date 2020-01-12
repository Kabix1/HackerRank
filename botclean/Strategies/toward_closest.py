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


def find_closest_dirt(pos, board, max_distance=0):
    if not max_distance:
        max_distance = len(board) + len(board[0])
    n_moves = 1
    start = (pos[0] + n_moves, pos[1])
    curr = list(start)
    dx, dy = -1, 1
    while n_moves <= max_distance:
        if is_dirt(curr, board):
            return curr
        curr[0] += dx
        curr[1] += dy
        if curr[0] == pos[0]:
            dy = -dy
        if curr[1] == pos[1]:
            dx = -dx
        if curr == list(start):
            n_moves += 1
            start = (pos[0] + n_moves, pos[1])
            curr = list(start)


def _next_move(pos, board):
    if board[pos[0]][pos[1]] == DIRT:
        return "CLEAN"
    closest = find_closest_dirt(pos, board)
    vector = [closest[0] - pos[0], closest[1] - pos[1]]
    dir = ""
    if vector[0]:
        dir = "DOWN" if vector[0] > 0 else "UP"
    else:
        dir = "RIGHT" if vector[1] > 0 else "LEFT"
    return dir
