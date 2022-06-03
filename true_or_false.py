"""
Checking if a variable is True
$ python -m timeit -s "variable=False" "if variable == True: pass"
11 nsec
$ python -m timeit -s "variable=False" "if variable is True: pass"
8.28 nsec  (11/8.28 = 1.33)
$ python -m timeit -s "variable=False" "if variable: pass"
6.25 nsec (11/6.25 = 1.76)

or not True
$ python -m timeit -s "variable=False" "if variable != True: pass"
10.5 nsec
$ python -m timeit -s "variable=False" "if variable is not True: pass"
8.08 nsec (10.5/8.08 = 1.3)
$ python -m timeit -s "variable=False" "if not variable: pass"
5.15 nsec (10.5/5.15 = 2.03)

"if variable" or "if not variable" is usually the most concise and fastest way.
But it doesn't distinguish between True and truthy values (basically anything that evaluates to True when passed to bool() function, so "1", "some text", etc.)
If you need to distinguish True from any other truthy value ("some string", 1, etc.), use "if variable is True" (True is a singleton, so identify comparison "is" is faster than equality comparison "==").

See a more detailed explanation: https://switowski.com/blog/checking-for-true-or-false
"""
