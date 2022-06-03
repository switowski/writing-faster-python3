# permission_vs_forgiveness_alt.py

"""
Ask for permission vs. ask for forgiveness when checking for 1 attribute.

Alternative version that doesn't use a global FOO object, but initializes an instance of class Foo() inside each test function.

python -m timeit -s "from permission_vs_forgiveness_alt import test_permission" "test_permission()"
117 nsec
python -m timeit -s "from permission_vs_forgiveness_alt import test_forgiveness" "test_forgiveness()"
91.2 nsec (117/91.2 = 1.28)

The difference between both functions is now larger, but both functions run slower than using a global object (class initialization takes longer than global object lookup).
I will stick with global FOO object in the presentation, but it doesn't really matter how you initialize the object.
"""

class BaseClass:
    hello = "world"

class Foo(BaseClass):
    pass

# Ask for permission
def test_permission():
    FOO = Foo()
    if hasattr(FOO, "hello"):
        FOO.hello

# Ask for forgiveness
def test_forgiveness():
    FOO = Foo()
    try:
        FOO.hello
    except AttributeError:
        pass
