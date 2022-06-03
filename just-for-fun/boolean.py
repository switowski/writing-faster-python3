"""
You can check the boolean value in a faster way:

python -m timeit -s "a = True" "bool(a)"
21.5 nsec

python -m timeit -s "a = True" "not not a"
9.89 nsec

Using keywords will always be faster than using functions
(even those built-in because interpreter still needs to check if you overrode it).
"""
