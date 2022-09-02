import numpy as np

size = 21



ways = np.zeros((size, size))

ways[size-1, size-1] = 1


for start in range((size - 1) * 2 - 1, -1, -1):
    x = start
    while x >= 0:
        if x < size and start - x < size:
            y = start - x
            s = 0
            if x < size - 1:
                s += ways[x + 1, y]
            if y < size - 1:
                s += ways[x, y + 1]
            ways[x, y] = s
            print(x, y, s)

            
        x -= 1

print(ways)
print(f"The answer is {ways[0, 0]}")


