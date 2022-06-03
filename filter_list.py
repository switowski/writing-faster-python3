# filter_list.py

"""
Filter a list

python -m timeit -s "from filter_list import test_loop" "test_loop()"
33.5 msec

python -m timeit -s "from filter_list import test_filter" "test_filter()"
49.9 msec

python -m timeit -s "from filter_list import test_comprehension" "test_comprehension()"
25.9 msec

"""

NUMBERS = range(1_000_000)


def test_loop():
    odd = []
    for number in NUMBERS:
        if number % 2:
            odd.append(number)
    return odd


# It's slower because the list creation takes time
# But if you don't need to create a list and can use the iterator returned from filter(), it's a good solution
def test_filter():
    return list(filter(lambda x: x % 2, NUMBERS))

def test_comprehension():
    return [number for number in NUMBERS if number % 2]
