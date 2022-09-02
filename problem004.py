biggest_number = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = str(i * j)
        if n == n[::-1] and int(n) > biggest_number:
            biggest_number = int(n)

print(f"The answer is {biggest_number}")

