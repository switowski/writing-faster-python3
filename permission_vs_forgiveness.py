# Ask for permission vs ask for forgiveness when checking for 1 attribute
class BaseClass:
    hello = "world"

class Foo(BaseClass):
    pass

FOO = Foo()

def test_permission():
    if hasattr(FOO, "hello"):
        FOO.hello

# Ask for forgiveness
def test_forgiveness():
    try:
        FOO.hello
    except AttributeError:
        pass
