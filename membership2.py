"""
Check if a specific number exists in a list vs. in a set

Element at the beginning of the list
python -m timeit -s "from membership2 import test_in" "test_in(42)"
301 nsec
python -m timeit -s "from membership2 import test_in_set" "test_in_set(42)"
45.9 nsec (301/45.9 = 6.56)
python -m timeit -s "from membership2 import test_in_set_proper" "test_in_set_proper(42)"
11.8 msec (11800000/301 = 39,203)

Element at the end of the list
python -m timeit -s "from membership2 import test_in" "test_in(999_958)"
6.04 msec
python -m timeit -s "from membership2 import test_in_set" "test_in_set(999_958)"
51.5 nsec (6040000/51.5 = 117,282)
python -m timeit -s "from membership2 import test_in_set_proper" "test_in_set_proper(999_958)"
11.9 msec (11.9/6.04 = 1.97)

Element does not exist:
python -m timeit -s "from membership2 import test_in" "test_in(-5)"
5.87 msec
python -m timeit -s "from membership2 import test_in_set" "test_in_set(-5)"
46.1 nsec (5870000/46.1 = 127,332)
python -m timeit -s "from membership2 import test_in_set_proper" "test_in_set_proper(-5)"
11.8 msec (11.8/5.87 = 2.01)

How long does it take convert a list to a set?
python -m timeit -s "MILLION_NUMBERS = list(range(1_000_000))" "set(MILLION_NUMBERS)"
11.8 msec
Converting list to a set takes most of the time in the previous benchmarks.

How long does it take to create a set vs. create a list?
python -m timeit "list(range(1_000_000))"
13 msec
python -m timeit "set(range(1_000_000))"
21.7 msec
Creating set is much slower than creating a list
"""

MILLION_NUMBERS = list(range(1_000_000))
MILLION_NUMBERS_SET = set(MILLION_NUMBERS)

def test_in(number):
    return number in MILLION_NUMBERS

def test_in_set(number):
    return number in MILLION_NUMBERS_SET

def test_in_set_proper(number):
    return number in set(MILLION_NUMBERS)
