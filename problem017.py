"""
Let me start by saying I hate this problem
"""

ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
ugh = {"11": 6, "12": 6, "13": 8, "14": 8, "15": 7, "16": 7, "17": 9, "18": 8, "19": 8}
twos = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]


s = sum(ones) + 11  # ones and one thousand
for i in range(10, 1000):
    _s = 0
    if i > 100:
        _s += ones[int(str(i)[0])] + 10  # hundred and = 10
    if str(i)[-2:] in ugh:
        _s += ugh[str(i)[-2:]]

    else:
        two, one = str(i)[-2:]
        two, one = int(two), int(one)
        _s += twos[two] + ones[one]

    s += _s

print(f"The answer is {s}")
