from copy import deepcopy

digits = 5
d_n = 30


def generate_paths(digits: int, start: list = None):
    if start is None:
        cutoff = 9
        start = []
    else:
        if len(start) == digits:
            return [start]
        cutoff = start[-1]

    results = []
    for i in range(cutoff + 1):
        new_start = deepcopy(start)
        new_start.append(i)
        results.extend(generate_paths(digits=digits, start=new_start))
    return results


def extend(digits: int, d_n: int = None, start: list = None, cutoff: int = 9):
    if d_n is None:
        d_n = digits * 9
    if start is None:
        start = []
    if digits == 0:
        return [start]

    results = []
    for i in range(min(cutoff, d_n)):
        new_start = deepcopy(start)
        new_start.append(i)
        results.extend(extend(digits-1, d_n=d_n-i, start=new_start, cutoff=i))
    return results

import time
start = time.time()
generate_paths(18)
print(round(time.time() - start, 2))
