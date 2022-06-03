"""
Check if a specific number exists in a list

Element at the beginning of the list
python -m timeit -s "from membership import test_for_loop" "test_for_loop(42)"
591 nsec
python -m timeit -s "from membership import test_in" "test_in(42)"
300 nsec (591/300 = 1.97)

Element at the end of the list
python -m timeit -s "from membership import test_for_loop" "test_for_loop(999_958)"
12.7 msec
python -m timeit -s "from membership import test_in" "test_in(999_958)"
6.02 msec (12.7/6.02 = 2.11)

Element does not exist:
python -m timeit -s "from membership import test_for_loop" "test_for_loop(-5)"
12.7 msec
python -m timeit -s "from membership import test_in" "test_in(-5)"
5.87 msec (12.7/5.87 = 2.16)
"""

MILLION_NUMBERS = list(range(1_000_000))

def test_for_loop(number):
    for item in MILLION_NUMBERS:
        if item == number:
            return True
    return False

def test_in(number):
    return number in MILLION_NUMBERS
