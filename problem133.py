import time


primes = [2]

N = 100000

for i in range(3, N):
    for j in primes:
        if j > i ** .5:
            primes += [i]
            break
        if i % j == 0:
            break

def is_valid(i):
    while i > 1:
        if i % 2 == 0:
            i //= 2
            continue
        if i % 5 == 0:
            i //= 5
            continue
        return False

    return True

def get_candidates(prime):
    return [i for i in range(1, prime + 1) if is_valid(i)]

start = time.time()

s = 0

for p in primes:
    for candidate in get_candidates(p):
        n = int("1" * candidate)
        if n % p == 0:
            print(p, candidate)
            s += p
            break


print(f"It took {time.time() - start:.2f} seconds to calculate for {N}\n"
        f"The answer is: {sum(primes) - s}")


