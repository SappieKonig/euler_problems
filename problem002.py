condition = lambda x: x % 2 == 0
fibonacci = [1, 2]

while fibonacci[-1] <= 4e6:
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

print(sum([i for i in fibonacci if condition(i)]))
