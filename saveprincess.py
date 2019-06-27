#!/usr/bin/env python


def displayPathtoPrincess(grid):
    x_m, y_m = -1, -1
    x_p, y_p = -1, -1
    for y, row in enumerate(grid):
        if row.find("m") >= 0:
            x_m = row.find("m")
            y_m = y
        if row.find("p") >= 0:
            x_p = row.find("p")
            y_p = y
    x_movement = x_p - x_m
    y_movement = y_p - y_m
    if x_movement < 0:
        print("\n".join(["LEFT"] * abs(x_movement)))
    while x_movement > 0:
        print("RIGHT")
        x_movement -= 1
    while y_movement < 0:
        print("UP")
        y_movement += 1
    while y_movement > 0:
        print("DOWN")
        y_movement -= 1


if __name__ == "__main__":
    displayPathtoPrincess(["___", "__m", "p__"])
