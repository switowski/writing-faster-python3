"""
Different ways to merge dictionaries

3 dictionaries:
python -m timeit -s "from merge_dict import test_update" "test_update()"
2.72 usec
python -m timeit -s "from merge_dict import test_unpacking" "test_unpacking()"
2.65 usec
python -m timeit -s "from merge_dict import test_union" "test_union()"
3.01 usec

See https://peps.python.org/pep-0584/ for nice writeup of existing ways and proposal of the union operator
The new union operator is slower for 3 dictionaries.

2 dictionaries:
python -m timeit -s "from merge_dict import test_update_2_dicts" "test_update_2_dicts()"
1.32 usec
python -m timeit -s "from merge_dict import test_unpacking_2_dicts" "test_unpacking_2_dicts()"
1.27 usec
python -m timeit -s "from merge_dict import test_union_2_dicts" "test_union_2_dicts()"
1.27 usec

But, if we are merging 2 dictionaries, the new operator is as fast as the unpacking!
"""

dict_a = {x: x*x for x in range(100)}
dict_b = {x: x*x for x in range(50, 150)}
dict_c = {x: x*x for x in range(100, 200)}

def test_update():
    out = dict_a.copy()  # Let's not modify dict_a in place
    out.update(dict_b)
    out.update(dict_c)
    return out

def test_unpacking():
    return {**dict_a, **dict_b, **dict_c}

# Requires Python 3.9
def test_union():
    return dict_a | dict_b | dict_c

# Test same checks, but for 2 dictionaries instead of 3
def test_update_2_dicts():
    out = dict_a.copy()  # Let's not modify dict_a in place
    out.update(dict_b)
    return out

def test_unpacking_2_dicts():
    return {**dict_a, **dict_b}

# Requires Python 3.9
def test_union_2_dicts():
    return dict_a | dict_b
