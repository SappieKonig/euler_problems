from utils import get_primes_until

# get enough of em just to be sure
primes = get_primes_until(1_000_000)
print(f"The answer is {primes[10000]}")
