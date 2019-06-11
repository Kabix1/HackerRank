#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pi_distance
import pi_distance2
import decimal


def plot(diffs, diffs2=None):
    x = [diff.d for diff in diffs]
    y = [diff.diff for diff in diffs]
    if diffs2:
        x2 = [diff.d for diff in diffs2]
        y2 = [diff.diff for diff in diffs2]
        plt.plot(x, y, "k", x2, y2, ".", linewidth=0.5)
    else:
        plt.plot(x, y, linewidth=0.5)
    plt.yscale("log")

if __name__ == "__main__":
    cont_diffs = []
    min, max = int(2.9*10**5), int(3.1*10**5)
    for i in range(1, 10):
        cont = pi_distance.PI_CONT[:i]
        cont_diffs.append(pi_distance.PI_dist(cont))
    for j in range(4, 10):
        cont = pi_distance.PI_CONT[:j+1]
        for i in range(round(cont[j] - 10), round(cont[j] + 20)):
            cont[j] = i
            cont_diffs.append(pi_distance.PI_dist(cont))
    cont_diffs2 = list(cont_diffs)
    for diff in cont_diffs2:
        for i in range(2, 10):
            cont_diffs.append(pi_distance.PI_dist(diff.d*i))
    raw_num = len(cont_diffs)
    # cont_diffs.append(pi_distance.PI_dist([3, 7, 15, 1, 301, 1, 1, 4]))
    cont_diffs = list(filter(lambda x: min <= x.d <= max, cont_diffs))
    print(len(cont_diffs))

    diffs = []
    for i in range(min, max):
        diffs.append(pi_distance.PI_dist(i))
    diffs2 = pi_distance.get_minimas(diffs)
    diffs3 = pi_distance.get_minimas(diffs2)
    diffs4 = pi_distance.get_minimas(diffs3)

    # plt.subplot(4, 1, 3)
    ds = [diff.d for diff in diffs3]
    cont_diffs_matches = list(filter(lambda x: x.d in ds, cont_diffs))
    final_num = len(cont_diffs_matches)
    print(final_num, final_num / raw_num)
    for diff in cont_diffs_matches:
        print(diff.d, diff.cont_frac)
    # for diff in diffs3:
    #     print(diff.d, diff.cont_frac)
    # plot(diffs2, cont_diffs)
    # plt.show()


if __name__ == "__live_coding__":
    continued_fraction = [3, 7, 15, 1, 292]
    d = decimal.Decimal("0")
    n = decimal.Decimal("1")
    for num in continued_fraction[-1::-1]:
        d += n * num
        d, n = n, d
    n = (((285 + 1) * 15 + 285) * 7 + 286) * 3 + 4575
    d = ((285 + 1) * 15 + 285) * 7 + (285 + 1)
    t = 16*7+1
    d = pi_distance.get_d(continued_fraction)

