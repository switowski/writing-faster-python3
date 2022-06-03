"""
Two ways to create a dictionary

Empty dictionary:
python -m timeit "a = dict()"
38.3 nsec
python -m timeit "a = {}"
14 nsec (38.3/14 = 2.7)

Non-empty dictionary:
python -m timeit "a = dict(a=1, b=2)"
68.1 nsec
python -m timeit "a = {'a':1, 'b':2}"
41.5 nsec (68.1/41.5 = 1.64)

Curious what's going on? Start Python REPL and run:
from dis import dis
dis("dict()")
dis("{}")

The shorthand doesn't have to load the name and call function.
It just runs the operation for initializing the dictionary straight away.
"""
