import numpy as np
import numba as nb

@nb.njit
def get_primes_until(m: int) -> np.array:
    if m < 2:
        return np.array([0])[:0]
    if m == 2:
        return np.array([2])
    primes = np.full((m,), True)
    # set 0 and 1 to not be a prime
    primes[:2] = False
    for i in range(m):
        if primes[i]:
            primes[i ** 2::i] = False

    return np.arange(m)[primes]



