"""
Building a dictionary vs. dictionary comprehension

python -m timeit -s "from building_dictionary import test_for_loop" "test_for_loop()"
61.2 ms
python -m timeit -s "from building_dictionary import test_pairs" "test_pairs()"
96.5 ms
Second version is slower because first we construct a large list and then we construct a dictionary from it. Probably memory usage is unnecessarily high.

python -m timeit -s "from building_dictionary import test_for_loop" "test_for_loop()"
60.5 ms
python -m timeit -s "from building_dictionary import test_comprehension" "test_comprehension()"
58.8 ms
Almost the same, but dictionary comprehension looks much nicer

"""

NUMBERS = range(1_000_000)

def test_for_loop():
    dictionary = {}
    for number in NUMBERS:
        dictionary[number] = number * number
    return dictionary

def test_pairs():
    return dict([(number, number*number) for number in NUMBERS])

def test_comprehension():
    return {number: number*number for number in NUMBERS}
