# permission_vs_forgiveness2.py

"""
Ask for permission vs. ask for forgiveness when checking for 3 attributes

python -m timeit -s "from permission_vs_forgiveness2 import test_permission" "test_permission()"
151 nsec
python -m timeit -s "from permission_vs_forgiveness2 import test_forgiveness" "test_forgiveness()"
82.9 nsec (151/82.9 = 1.82)
"""

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

# Ask for forgiveness
def test_forgiveness():
    try:
        FOO.hello
        FOO.bar
        FOO.baz
    except AttributeError:
        pass
