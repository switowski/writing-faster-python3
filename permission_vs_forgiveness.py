# permission_vs_forgiveness.py

"""
Ask for permission vs. ask for forgiveness when checking for 1 attribute

python -m timeit -s "from permission_vs_forgiveness import test_permission" "test_permission()"
71.1 nsec
python -m timeit -s "from permission_vs_forgiveness import test_forgiveness" "test_forgiveness()"
61.6 nsec (71.1/61.6 = 1.15)
"""

class BaseClass:
    hello = "world"

class Foo(BaseClass):
    pass

FOO = Foo()

# Ask for permission
def test_permission():
    if hasattr(FOO, "hello"):
        FOO.hello

# Ask for forgiveness
def test_forgiveness():
    try:
        FOO.hello
    except AttributeError:
        pass
