"""
python -m timeit -s "from tuple_vs_namedtuple import test_tuple" "test_tuple()"
67 nsec
python -m timeit -s "from tuple_vs_namedtuple import test_namedtuple" "test_namedtuple()"
16.2 usec

Namedtuple is obviously slower, but so much more understandable.
"""
from collections import namedtuple


def test_tuple():
    point = (1, 20)
    x = point[0]
    y = point[1]

def test_namedtuple():
    Point = namedtuple("Point", ["x", "y"])
    point = Point(x=1, y=20)
    x = point.x
    y = point.y
