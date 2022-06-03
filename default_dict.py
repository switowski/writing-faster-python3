"""
Using defaultdict vs. manually setting the initial value of a new key in a dictionary.

python -m timeit -s "from default_dict import test_slow" "test_slow()"
57.6 ms
python -m timeit -s "from default_dict import test_fast" "test_fast()"
43.3 ms (57.6/43.3 = 1.33)

Since we are counting things, we can further improve our code by using the Counter():
python -m timeit -s "from default_dict import test_fast" "test_fast()"
43.3 ms
python -m timeit -s "from default_dict import test_counter" "test_counter()"
26.5 ms (43.3/26.5 = 1.63)

"""
from collections import Counter, defaultdict
from random import randrange

DUPLICATES = [randrange(100) for _ in range(1_000_000)]


def test_slow():
    d = {}
    for number in DUPLICATES:
        if number not in d:
            d[number] = 1
        else:
            d[number] += 1
    return d

# defaultdict(int) is equivalent to defaultdict(lambda: 0)
def test_fast():
    d = defaultdict(int)
    for number in DUPLICATES:
        d[number] += 1
    return d

# Bonus: for counting stuff, use the Counter
def test_counter():
    return Counter(DUPLICATES)

