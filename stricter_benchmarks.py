"""
Example of a stricter benchmarks where we always run the same number of loops and we only allow 1 run (so no repetition).
Run it:
python stricter_benchmarks.py
Then comment out line 45, uncomment line 46 and run it again:
python stricter_benchmarks.py

Using stricter benchmarks doesn't really add that much value.
Some random processes running on your computer will affect the benchmarks more than we improve them with those tiny tweaks.
Just try to run benchmarks a couple of times and each time you will get a slightly different number.
And still, one might argue if running the code once instead of 5 times is a better or worse benchmark.
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


if __name__ == "__main__":
    # To make the benchmark even more strict, we can explicitly set the number of loops to run and we execute only one
    # function at a time to prevent any caching
    import timeit

    NUMBER = 2_000_000
    print(timeit.timeit("test_permission()", setup="from __main__ import test_permission", number=NUMBER))
    # print(timeit.timeit("test_forgiveness()", setup="from __main__ import test_forgiveness", number=NUMBER))
