from utils import get_primes_until


n = 20
primes = get_primes_until(n + 1)

s = 1

for prime in primes:
    r = prime
    while r * prime < n:
        r *= prime
    s *= r

print(f"The answer is {s}")
