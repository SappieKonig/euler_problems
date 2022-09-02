numbers = range(1, 101)

print(f"The answer is {sum(numbers) ** 2 - sum(map(lambda x: x ** 2, numbers))}")
