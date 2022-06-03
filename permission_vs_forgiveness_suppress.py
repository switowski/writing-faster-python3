# permission_vs_forgiveness_suppress.py

"""
Alternative version of asking for forgiveness  - here we use suppress() function from the contextlib module to explicitly suppress the exception instad of putting "pass" inside "except" block.

python -m timeit -s "from permission_vs_forgiveness_suppress import test_permission" "test_permission()"
149 nsec
python -m timeit -s "from permission_vs_forgiveness_suppress import test_pass" "test_pass()"
84.9 nsec
python -m timeit -s "from permission_vs_forgiveness_suppress import test_suppress" "test_suppress()"
347 nsec (347/84.9 = 4.09)

Using suppress function is 4 times as slow as putting "pass" statement in the except block (and even if the exception is actually thrown, suppress is still around twice as slow as "pass" statement).
But suppress() is a very good way of showing that you explicitly want to ignore that exception.
"""

import contextlib

class BaseClass:
    hello = "world"
    bar = "world"
    baz = "world"

class Foo(BaseClass):
    pass

FOO = Foo()

# Ask for permission
def test_permission():
    if hasattr(FOO, "hello") and hasattr(FOO, "bar") and hasattr(FOO, "baz"):
        FOO.hello
        FOO.bar
        FOO.baz

# Ask for forgiveness with pass
def test_pass():
    try:
        FOO.hello
        FOO.bar
        FOO.baz
    except AttributeError:
        pass

# Ask for forgiveness with suppress
def test_suppress():
    with contextlib.suppress(AttributeError):
        FOO.hello
        FOO.bar
        FOO.baz
