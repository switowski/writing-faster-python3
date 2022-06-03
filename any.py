"""
Replace multiple "or" checks with one "any" check

python -m timeit -s "from any import test_or" "test_or()"
57.4 nsec

python -m timeit -s "from any import test_any" "test_any()"
113 nsec

Any is much slower due to list construction overhead.
"""

a,b,c,d,e,f = 0,0,0,1,0,0

def test_or():
    if a or b or c or d or e or f:
        return 1
    return 0

def test_any():
    if any([a, b, c, d, e, f]):
        return 1
    return 0
