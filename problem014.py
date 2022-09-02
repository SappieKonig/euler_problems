chain_mapping = {}


for i in range(1, 1_000_000):
    steps = 0
    # integers are immutable, no need for copying
    n = i
    while n != 1:
        if n in chain_mapping:
            steps += chain_mapping[n]
            break
        steps += 1
        if n % 2 == 0:
            n //= 2
            continue
        n = n * 3 + 1
            
    chain_mapping[i] = steps

best = None
m = -1
for k, v in chain_mapping.items():
    if v > m:
        best = k
        m = v

print(f"The answer is {best}")
