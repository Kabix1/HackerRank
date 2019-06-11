import decimal
import collections

PI = decimal.Decimal("3.141592653589793238462643383279502884197169399375105820974944592307816406286")

PI_CONT = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1]


def get_continued_fraction(fraction):
    continued_fraction = []
    d, q = fraction
    while q and d:
        i = int(q/d)
        continued_fraction.append(i)
        q -= i*d
        q, d = d, q
    return continued_fraction


def get_d(continued_fraction):
    d = decimal.Decimal("0")
    n = decimal.Decimal("1")
    for num in continued_fraction[-1::-1]:
        d += n * num
        d, n = n, d
    return d

class PI_dist:
    def __init__(self, arg):
        if isinstance(arg, collections.abc.Sequence):
            self.cont_frac = arg
            self.d = get_d(arg)
            self.n = round(self.d * PI)
        else:
            self.d = arg
            self.n = round(self.d * PI)
            self.cont_frac = get_continued_fraction((self.d, self.n))
        self.diff = abs(decimal.Decimal(self.n/self.d) - PI) if self.d else 1

    def __str__(self):
        return "n: {}, d: {}, diff: {:.2e}".format(self.n, self.d, self.diff)


def get_minimas(diffs):
    minimas = []
    for i, n in enumerate(diffs[1:-1]):
        if diffs[i-1].diff > diffs[i].diff < diffs[i+1].diff:
            minimas.append(diffs[i])
    return minimas

if __name__ == "__main__":
    print("Hej")
