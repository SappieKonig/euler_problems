import numba as nb


m = 25_000_000

triples = set()


@nb.njit
def solve():
    triples = set()
    for a in range(m):
        if not (a % 1000):
            print(f"We are at {a} (hint, that's much too slow)")
        for b in range(a + 1, m):
            if (b - a) ** 2 * 3 > 2 * a * b:
                break
            c = int((a ** 2 + b ** 2) ** .5)
            if c ** 2 == a ** 2 + b ** 2 and c % (b - a) == 0:
                triples.add((a, b, c))
                print(a, b, c)


print(solve())
