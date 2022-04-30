# Ask for permission vs ask for forgiveness when checking for 3 attributes
class BaseClass:
    hello = "world"
    bar = "world"
    baz = "world"

class Foo(BaseClass):
    pass

FOO = Foo()

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
