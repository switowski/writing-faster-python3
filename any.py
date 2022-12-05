"""
Replace multiple "or" checks with one "any" check

python -m timeit -s "from any import test_or" "test_or()"
72.1 nsec
python -m timeit -s "from any import test_any" "test_any()"
149 nsec

Any is much slower. Is it because of the list construction overhead?

python -m timeit -s "from any import test_any_existing_list" "test_any_existing_list()"
86.1 nsec

There is some overhead that we can eliminate by building the list outside of the benchmarked function.
But still, any is slower than or.

Let's also check different combinations with all elements being 1 or 0 and when 1 is found first vs. when it's last:

python -m timeit -s "from any import test_or_zeroes" "test_or_zeroes()"
97.1 nsec per loop
python -m timeit -s "from any import test_any_zeroes" "test_any_zeroes()"
97.4 nsec per loop

python -m timeit -s "from any import test_or_ones" "test_or_ones()"
44.2 nsec per loop
python -m timeit -s "from any import test_any_ones" "test_any_ones()"
75.9 nsec per loop

python -m timeit -s "from any import test_or_start" "test_or_start()"
44.2 nsec per loop
python -m timeit -s "from any import test_any_start" "test_any_start()"
76.8 nsec per loop

python -m timeit -s "from any import test_or_end" "test_or_end()"
93.9 nsec per loop
python -m timeit -s "from any import test_any_end" "test_any_end()"
93.1 nsec per loo

"or" short-circuits the evaluation, so if the first argument is True, it stops. Any will evaluate all it's arguments.
This is especially visible for the test_or_ones() and test_or_start() functions, where the first argument is "1" so we
stop the checking and "or" finishes much faster than "any()".


See this StackOverflow question for more details: https://stackoverflow.com/questions/22510205/all-vs-and-and-any-vs-or
One useful use-case for any() is when you want to check a variable number of arguments, like:
if any(isOdd(x) for x in data)
"""

a,b,c,d,e,f = 0,0,0,1,0,0
list_abcdef = [a, b, c, d, e, f]

def test_or():
    if a or b or c or d or e or f:
        return 1
    return 0

def test_any():
    if any([a, b, c, d, e, f]):
        return 1
    return 0

def test_any_existing_list():
    if any(list_abcdef):
        return 1
    return 0


a1,b1,c1,d1,e1,f1 = 0,0,0,0,0,0
a2,b2,c2,d2,e2,f2 = 1,1,1,1,1,1
a3,b3,c3,d3,e3,f3 = 1,0,0,0,0,0
a4,b4,c4,d4,e4,f4 = 0,0,0,0,0,1

list_a1 = [a1, b1, c1, d1, e1, f1]
list_a2 = [a2, b2, c2, d2, e2, f2]
list_a3 = [a3, b3, c3, d3, e3, f3]
list_a4 = [a4, b4, c4, d4, e4, f4]

def test_or_zeroes():
    if a1 or b1 or c1 or d1 or e1 or f1:
        return 1
    return 0

def test_any_zeroes():
    if any(list_a1):
        return 1
    return 0

def test_or_ones():
    if a2 or b2 or c2 or d2 or e2 or f2:
        return 1
    return 0

def test_any_ones():
    if any(list_a2):
        return 1
    return 0

def test_or_start():
    if a3 or b3 or c3 or d3 or e3 or f3:
        return 1
    return 0

def test_any_start():
    if any(list_a3):
        return 1
    return 0

def test_or_end():
    if a4 or b4 or c4 or d4 or e4 or f4:
        return 1
    return 0

def test_any_end():
    if any(list_a4):
        return 1
    return 0
