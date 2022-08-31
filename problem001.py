condition = lambda x: x % 3 == 0 or x % 5 == 0
print(f"The answer is {sum([i for i in range(1000) if condition(i)])}")
