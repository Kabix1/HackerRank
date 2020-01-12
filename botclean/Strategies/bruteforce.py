#!/usr/bin/env python

import itertools

ROUTE = []


def calc_dist(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])


def tsp_bruteforce(graph, s):
    vertex = []
    for i in range(len(graph)):
        if not i == s:
            vertex.append(i)

    min_path = [999999999999, None]

    for perm in itertools.permutations(vertex):
        current_pathweight = 0

        k = s
        for v in perm:
            current_pathweight += graph[k][v]
            k = v

        min_path = [current_pathweight, perm
                    ] if current_pathweight < min_path[0] else min_path
    return min_path


def pos2moves(pos1, pos2):
    vector = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
    vertical_num = abs(vector[0])
    horisontal_num = abs(vector[1])
    vertical = ["DOWN"] if vector[0] > 0 else ["UP"]
    horisontal = ["RIGHT"] if vector[1] > 0 else ["LEFT"]
    moves = vertical * vertical_num
    moves.extend(horisontal * horisontal_num)
    return moves


def path2moves(start, path):
    moves = []
    pos1 = start
    for pos in path:
        temp = pos2moves(pos1, pos)
        moves.extend(temp)
        pos1 = pos
    return moves


def _next_move(pos, board):
    global ROUTE
    if "b" not in board:
        return "CLEAN"
    if not ROUTE:
        # dirt = np.argwhere(board == "d")
        dirt = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == "d":
                    dirt.append((i, j))
        positions = [pos]
        positions.extend(dirt)
        graph = []
        for pos1 in positions:
            graph.append([calc_dist(pos1, pos2) for pos2 in positions])
        min_path = tsp_bruteforce(graph, 0)
        path = [positions[i] for i in min_path[1]]
        ROUTE = path2moves(pos, path)
    return ROUTE.pop(0)
