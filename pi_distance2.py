#!/usr/bin/env python
import nose
import random
import collections
import decimal


PI = decimal.Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914")
PI_CONT = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1]


def get_factors(num):
    factors = []
    for i in range(2, int(num/2) + 1):
        if not num%i:
            factors.append(i)
    return factors


def calc_continued_fraction(val, num=100):
    p = val
    continued_fraction = []
    for _ in range(num - 1):
        i = int(p)
        continued_fraction.append(i)
        if i == p:
            return continued_fraction
        p = 1 / (p - i)
    continued_fraction.append(round(p))
    return continued_fraction


def simplify_fraction(frac):
    q_factors = get_factors(frac[1])
    d_factors = get_factors(frac[0])
    gcd = max(set(q_factors)&set(d_factors)^{1})
    return (frac[0]/gcd, frac[1]/gcd)


def is_local_minima(arg):
    if isinstance(arg, collections.abc.Sequence):
        d = arg[0]
    else:
        d = arg
    dist = calc_dist(d)
    return calc_dist(d-1) > dist < calc_dist(d+1)


def get_continued_fraction(fraction):
    continued_fraction = []
    d, q = fraction
    while q and d:
        i = int(q/d)
        continued_fraction.append(i)
        q -= i*d
        q, d = d, q
    return continued_fraction


def test_pi_distance():
    for _ in range(100):
        min = random.randint(1,10000)
        max = random.randint(min, 999999)
        # min, max = 3336, 11009
        best_dist = 1
        best_d = 0
        for d in range(min, max + 1):
            pi_test = round(PI * d) / d
            dist = abs(pi_test - PI)
            if dist < best_dist:
                best_dist = dist
                best_d = d
        test = pi_dist(min, max)
        if best_d != test[0]:
            print(min, max)
            print(test)
            print(best_d, round(best_d*PI), round(best_d*PI)/best_d)
            print(get_continued_fraction((best_d, round(best_d*PI))))
        else:
            print("Correct")
        nose.tools.assert_equal(best_d, test[0])


def calc_dist(arg):
    if not isinstance(arg, collections.abc.Sequence):
        fraction = (arg, round(decimal.Decimal(arg)*PI))
    else:
        fraction = arg
    n = decimal.Decimal(fraction[1])
    d = decimal.Decimal(fraction[0])
    return abs(PI - n/d)


def simple_solution(min, max):
    best_dist = 99999999
    for d in range(min, max+1):
        dist = calc_dist(d)
        if dist < best_dist:
            best_d = d
            best_dist = dist
    return (best_d, round(best_d*PI))


def get_fraction(continued_fraction):
    d = decimal.Decimal("0")
    n = decimal.Decimal("1")
    for num in continued_fraction[-1::-1]:
        d += n * num
        d, n = n, d
    return (d,n)


def d2frac(d):
    return (d, round(d*PI))


def pi_dist(min, max):
    if min == max:
        return d2frac(min)
    d, i, dist = max, 0, 1
    best_fraction = (1, 1)

    d_next, _ = get_fraction(PI_CONT[:1])
    while d_next <= max:
        i += 1
        d = d_next
        cont_frac = PI_CONT[:i]
        d_next, _ = get_fraction(cont_frac)
    if min <= d <= max:
        best_fraction = d2frac(d)
        dist = calc_dist(best_fraction)

    cont = list(cont_frac)
    d = d_next
    while d > max:
        cont[-1] -= 1
        d_new, _ = get_fraction(cont)
        if d_new == d:
            break
        d = d_new
    if min <= d <= max and \
       (dist > calc_dist(d) or dist == calc_dist(d) and d < best_fraction[0]):
        dist = calc_dist(d)
        best_fraction = d2frac(d)

    cont = cont_frac[:-1]
    d, _ = get_fraction(cont)
    while d < min:
        cont[-1] += 1
        d_new, _ = get_fraction(cont)
        if d_new == d:
            break
        d = d_new
    d_next, _ = get_fraction(cont[:-1] + [cont[-1] + 1])
    while d_next <= max and calc_dist(d_next) < calc_dist(d):
        cont[-1] += 1
        d = d_next
        d_next, _ = get_fraction(cont[:-1] + [cont[-1] + 1])
    if min <= d <= max and \
       (dist > calc_dist(d) or dist == calc_dist(d) and d < best_fraction[0]):
        dist = calc_dist(d)
        best_fraction = d2frac(d)

    cont = cont_frac[:-1]
    d, _ = get_fraction(cont)
    k = int(min/d)
    if not k == min/d:
        k += 1
    d *= k
    if min <= d <= max and \
       (dist > calc_dist(d) or dist == calc_dist(d) and d < best_fraction[0]):
        assert d >= min
        dist = calc_dist(d)
        best_fraction = d2frac(d)

    cont[-1] += 1
    d, _ = get_fraction(cont)
    k = int(min/d)
    if not k == min/d:
        k += 1
    d *= k
    if min <= d <= max and \
       (dist > calc_dist(d) or dist == calc_dist(d) and d < best_fraction[0]):
        assert d >= min
        best_fraction = d2frac(d)

    if best_fraction == (1, 1):
        return simple_solution(min, max)
    return best_fraction




if __name__ == "__main__":
    # min, max = 10, 1000
    # q, d = pi_dist(min, max)
    frac = pi_dist(1, 10**15)
    print(calc_dist(frac))
    # test_pi_distance()
    # print(pi_dist2(5092, 67927))
