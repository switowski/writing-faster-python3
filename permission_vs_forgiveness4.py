# Ask for permission vs ask for forgiveness when 1 attribute doesn't exist
import contextlib
class BaseClass:
    hello = "world"
    # bar = "world"
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
    with contextlib.suppress(AttributeError):
        FOO.hello
        FOO.bar
        FOO.baz
