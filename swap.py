"""
Swap variables using a temporary variable vs. tuple assignment

python -m timeit -s "from swap import test_tmp_variable" "test_tmp_variable()"
47.6 nsec
python -m timeit -s "from swap import test_swap" "test_swap()"
45.3 nsec
"""

def test_tmp_variable():
    a = 1
    b = 2
    tmp = a
    a = b
    b = tmp


def test_swap():
    a = 1
    b = 2
    a, b = b, a
