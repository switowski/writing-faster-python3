"""
Chained vs. non-chained comparisons

python -m timeit -s "from chained import test_unchained" "test_unchained()"
54.2 nsec
python -m timeit -s "from chained import test_chained" "test_chained()"
56.8 nsec

Chained version is slightly slower.

If we disassemble both comparisons, we can see that "1 < x < 100" does more operations under the hood:
In [1]: dis.dis("1 < x < 100")
  1           0 LOAD_CONST               0 (1)
              2 LOAD_NAME                0 (x)
              4 DUP_TOP
              6 ROT_THREE
              8 COMPARE_OP               0 (<)
             10 JUMP_IF_FALSE_OR_POP     9 (to 18)
             12 LOAD_CONST               1 (100)
             14 COMPARE_OP               0 (<)
             16 RETURN_VALUE
        >>   18 ROT_TWO
             20 POP_TOP
             22 RETURN_VALUE

In [2]: dis.dis("x > 1 and x < 100")
  1           0 LOAD_NAME                0 (x)
              2 LOAD_CONST               0 (1)
              4 COMPARE_OP               4 (>)
              6 JUMP_IF_FALSE_OR_POP     8 (to 16)
              8 LOAD_NAME                0 (x)
             10 LOAD_CONST               1 (100)
             12 COMPARE_OP               0 (<)
             14 RETURN_VALUE
        >>   16 RETURN_VALUE
"""
def test_unchained():
    x = 10
    if x > 1 and x < 100:
        return True
    return False

def test_chained():
    x = 10
    if 1 < x < 100:
        return True
    return False
