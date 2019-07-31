import numpy as np
import bot
import curses
import timer
import time

COLORS = ['V', 'I', 'B', 'G', 'Y', 'O', 'R']
EMPTY = "-"
DIRS = np.array([(1, 0), (0, -1), (-1, 0), (0, 1)])
RIGHTMOST = -1


def print_board(board):
    print("#" * (board.shape[1] + 2))
    for row in board:
        s = "".join(row)
        print(f"#{s}#")
    print("#" * (board.shape[1] + 2))


def draw_board(stdscr, board):
    colors = ["-"] + COLORS
    for x in range(len(board)):
        for y in range(len(board[0])):
            stdscr.addstr(y, x, " ",
                          curses.color_pair(colors.index(board[x][y])))


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


def remove_group(board, pos):
    color = board[pos]
    assert color != EMPTY
    group = [pos]
    board[pos] = EMPTY
    for pos in group:
        for d in DIRS:
            pos2 = tuple(pos + d)
            if is_color(board, pos2, color):
                group.append(pos2)
                board[pos2] = EMPTY
    assert len(group) > 1


def generate_board(x: int, y: int, k: int) -> list:
    colors = COLORS[:k]
    board = np.random.choice(colors, size=(x, y))
    return board


def rule1(board):
    for column in board:
        scol = "".join(column)
        scol = f'{scol.replace(EMPTY, ""):->{board.shape[1]}}'
        column[:] = np.array(list(scol))


def rule2(board):
    global RIGHTMOST
    empty = [EMPTY] * board.shape[1]
    empty_columns = []
    for i, column in enumerate(board[:RIGHTMOST]):
        if list(column) == empty:
            # board[:, i:] = np.hstack(
            #     (board[:, i + 1:], np.array([[EMPTY] * board.shape[1]]).T))
            # RIGHTMOST -= 1
            empty_columns.append(i)
    for c in empty_columns[-1::-1]:
        cols = np.concatenate(
            (board[c + 1:, :], np.array([[EMPTY] * board.shape[1]])))
        board[c:, :] = cols
    RIGHTMOST -= len(empty_columns)


def init_curses():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_YELLOW)
    return stdscr


def count_blocks_left(board):
    return board.shape[0] * board.shape[1] - len(board[board == EMPTY])


def main():
    global RIGHTMOST
    stdscr = init_curses()
    x, y, k = 10, 20, 3
    num_games = 100

    blocks = 0
    for k in range(3, 7):
        board = generate_board(x, y, k)
        RIGHTMOST = x - 1
        done = False
        while not done:
            # print_board(board)
            draw_board(stdscr, board)
            stdscr.refresh()
            time.sleep(1)
            # print(bot.get_groups(board))
            # print(move)
            timer.start("bot")
            try:
                move = bot.next_move(x, y, board.tolist())
            except:
                timer.stop("bot")
                done = True
                break
            timer.stop("bot")
            timer.start("remove")
            try:
                remove_group(board, move)
            except:
                timer.stop("remove")
                done = True
                break
            timer.stop("remove")
            timer.start("rule1")
            rule1(board)
            timer.stop("rule1")
            timer.start("rule2")
            rule2(board)
            timer.stop("rule2")
        blocks += count_blocks_left(board)
    timer.result()
    print(blocks / num_games)


if __name__ == "__main__":
    main()
