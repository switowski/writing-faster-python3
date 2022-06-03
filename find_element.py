# find_element.py

"""
How to find an element in a collection of items that is matching a specific criteria.

python -m timeit -s "from find_element import while_loop" "while_loop()"
59.4 usec

python -m timeit -s "from find_element import for_loop" "for_loop()"
47 usec (59.4/47 = 1.26)

python -m timeit -s "from find_element import list_comprehension" "list_comprehension()"
254 usec (254/47 = 5.40)

python -m timeit -s "from find_element import generator" "generator()"
45.7 usec (47/45.7 = 1.03)
"""


# Let's find the first number divided by 42 and 43 (that's 1806).

def while_loop():
    number = 1
    while True:
        # You don't need to use parentheses, but they improve readability
        if (number % 42 == 0) and (number % 43 == 0):
            return number  # That's 1806
        number += 1

from itertools import count

def for_loop():
    for number in count(1):
        if (number % 42 == 0) and (number % 43 == 0):
            return number

def list_comprehension():
    return [n for n in range(1, 10_000) if (n % 42 == 0) and (n % 43 == 0)][0]

def generator():
    return next(n for n in count(1) if (n % 42 == 0) and (n % 43 == 0))
