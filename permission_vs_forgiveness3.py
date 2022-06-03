# permission_vs_forgiveness3.py

"""
Ask for permission vs. ask for forgiveness when an attribute doesn't exist

python -m timeit -s "from permission_vs_forgiveness3 import test_permission" "test_permission()"
81.4 nsec
python -m timeit -s "from permission_vs_forgiveness3 import test_forgiveness" "test_forgiveness()"
309 nsec (309/81.4 = 3.8)
"""

class BaseClass:
    hello = "world"
    # bar = "world"
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
