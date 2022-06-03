"""
Remove duplicates from a list

python -m timeit -s "from duplicates import test_for_loop" "test_for_loop()"
315 ms

python -m timeit -s "from duplicates import test_list_comprehension" "test_list_comprehension()"
315 ms

python -m timeit -s "from duplicates import test_set" "test_set()"
6.07 ms (315/6.07 = 51.89)

python -m timeit -s "from duplicates import test_dict" "test_dict()"
11 ms (315/11 = 28.64)
"""

from random import randrange

DUPLICATES = [randrange(100) for _ in range(1_000_000)]


def test_for_loop():
    unique = []
    for element in DUPLICATES:
        if element not in unique:
            unique.append(element)
    return unique

# That's a terrible way to use list comprehension, don't do that!
def test_list_comprehension():
    unique = []
    [unique.append(n) for n in DUPLICATES if n not in unique]
    return unique

def test_set():
    return list(set(DUPLICATES))

# Works only with hashable keys!
def test_dict():
    # Works in CPython 3.6 and above
    return list(dict.fromkeys(DUPLICATES))
