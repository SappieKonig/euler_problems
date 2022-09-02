from functools import cache

from utils import get_primes_until


primes = get_primes_until(1_000_000)


def get_prime_factorisation(n: int) -> list[int]:
    factors = []
    idx = 0
    while n > 1:
        if n % primes[idx] == 0:
            factors.append(primes[idx])
            n //= primes[idx]
            continue
        
        idx += 1
    return factors


def get_n_divisors(n: int) -> int:
    factors = get_prime_factorisation(n)

    n_divisors = 1
    for i in set(factors):
        n_divisors *= factors.count(i) + 1
    
    return n_divisors

@cache
def triangle(n: int) -> int:
    if n == 1:
        return 1
    return n + triangle(n-1)


n = 1
while 1:
    print(n)
    t = triangle(n)
    if get_n_divisors(t) > 500:
        print(f"The answer is {t}")
        break

    n += 1
