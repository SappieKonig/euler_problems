n = 1000

for a in range(n // 2):
    for b in range(a, n // 2):
        c = int((a ** 2 + b ** 2) ** .5)
        if c ** 2 == a ** 2 + b ** 2 and a + b + c == 1000:
            print(f"The answer is {a * b * c}")
