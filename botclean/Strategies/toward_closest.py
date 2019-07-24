def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def next_move(pos, board):
    # print(board)
    # print("b" in board)
    if board[pos[0]][pos[1]] == "d":
        return "CLEAN"
    dirt = []
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c == "d":
                dirt.append((i, j))
    bot = pos
    closest = None
    for pos in dirt:
        if not closest or dist(bot, pos) < closest[0]:
            closest = [dist(bot, pos), pos]
    vector = [closest[1][0] - bot[0], closest[1][1] - bot[1]]
    dir = ""
    if vector[0]:
        dir = "DOWN" if vector[0] > 0 else "UP"
    else:
        dir = "RIGHT" if vector[1] > 0 else "LEFT"
    return dir
