from utils import get_primes_until

n = 600851475143
primes = get_primes_until(10000)

biggest_divisor = 0

while n > 1:
    for prime in primes:
        if n % prime == 0:
            n //= prime
            biggest_divisor = prime
            break

print(f"The biggest divisor of {600851475143} is {biggest_divisor}")

