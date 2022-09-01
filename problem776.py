"""
Plan of attack: set d(n), then iterate over all numbers which have the same d(n)
Then loop over d(n), and easy peasy!
Generate all possible combinations using a brilliant algorithm.
Given a d(n) and a length of the target (so for example, 6 digits), go by all combinations.
But we can't brute force this, so: get all possible digit combinations, and count how many times they occur.
Then add all of these together and get your sum (explanatory addendum: count how many times every number comes in the nth place,
then sum this up, then add this to the)

"""
import time
from copy import deepcopy
from functools import cache


def simple_implementation(n: int):
    s = 0
    for i in range(1, n + 1):
        s += i / sum([int(j) for j in str(i)])
    return s


@cache
def factorial(x: int):
    if x == 0:
        return 1
    return x * factorial(x - 1)


def get_next_position(num: tuple[int]) -> tuple | None:
    # we are parsing back to front, so we take 1 from the very back (or almost the very back, 
    # if 3 charachters in the back all have the value 9,
    # we take the third from the back
    num = list(num)
    update_removal = True
    removal_index = len(num) - 1
    for i, j in zip(range(len(num) - 2, -1, -1), range(len(num) - 1, 0, -1)):
        if num[i] == num[j] and update_removal:
            removal_index = i
            continue

        update_removal = False
        
        # if the distance is 2 or more, we are actually sure that this is a new combination
        if num[-1] - num[i] >= 2:
            num[removal_index] -= 1
            num[i] += 1
            return tuple(num)

    return None  # signal that the update doesn't change anything
            

def initiate_num(d_n: int, digits: int):
    assert d_n >= 0
    assert d_n / digits <= 9

    num = [0] * digits  # we can do this because 0 is immutable, god references are annoying
    idx = digits - 1
    while d_n > 0:
        addition = min(9, d_n)
        d_n -= addition
        num[idx] = addition
        idx -= 1
    return tuple(num)


def get_possible_representations(d_n: int, digits: int):
    reps = [initiate_num(d_n, digits)]
    while 1:
        addition = get_next_position(reps[-1])
        if addition is None:
            return reps
        reps.append(addition)


def x_over_y(x: int, y: int) -> int:
    assert x >= y, "It's x over y, not y over x"
    return factorial(x) // (factorial(y) * factorial(x - y))


def get_number_of_rep_occurrences(num: tuple[int]) -> int:
    n = 1
    places_left = len(num)
    for i in range(10):
        occurances = num.count(i)
        n *= x_over_y(places_left, occurances)
        places_left -= occurances

    return n
       

def count_up_to_n_digits(digits: int):
    s = 0
    check = 0
    n = int("1" * digits)  # this needs a comment but I have no idea how to explain it
    for d_n in range(1, 9 * digits + 1):
        reps = get_possible_representations(d_n, digits)
        print(d_n, reps)
        for rep in reps:
            # average value of a digit multiplied by the total number of occurrences
            occurrences = get_number_of_rep_occurrences(rep)
            average_digit_value = occurrences / digits
            s += average_digit_value * n
            check += occurrences
    print(check)
    assert check + 1 == 10 ** digits
    return s


start = time.time()
print(count_up_to_n_digits(3))
print(f"The total time it took to do it the efficient way is {time.time() - start:.2f} seconds")

start = time.time()
print(simple_implementation(999))
print(f"The total time it took to do it the inefficient way is {time.time() - start:.2f} seconds")

