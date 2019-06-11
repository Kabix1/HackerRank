#!/usr/bin/env python

import math


def prime_factors(n):
    factors = {}
    end = int(n)
    for i in range(2, end + 1):
        while not n % i:
            if not i in factors:
                factors[i] = 1
            else:
                factors[i] += 1
            n /= i
    return factors


def factorialize(n):
    factors = {}
    values = list(range(1, n + 1))
    for n in values:
        new_factors = prime_factors(n)
        for key, value in new_factors.items():
            if key in factors:
                factors[key] += value
            else:
                factors[key] = value
    return factors


def solve(n, m):
    if m == 1:
        return 1
    m = m - 1
    n_fact = factorialize(n)
    m_fact = factorialize(m)
    sum_fact = factorialize(n+m)
    for key, value in m_fact.items():
        sum_fact[key] -= value
    for key, value in n_fact.items():
        sum_fact[key] -= value
    total = 1
    for key, value in sum_fact.items():
        total *= key**value % (10**9 + 7)
    return(int(total % (10**9 + 7)))


def solve2(n, m):
    mod = 10**9 + 7
    a = int(math.factorial(n+m-1))
    b = int(math.factorial(n))
    c = int(math.factorial(m-1))
    return (int(a/(b*c)) % mod)



print(solve(100,100))
print(solve2(100,100))
# m_fact = factorialize(list(range(1,9+1)))
# print(solve2(10,10))
# print(factorialize(list(range(101))))
