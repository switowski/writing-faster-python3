"""
You can assign values in a faster way

python -m timeit """a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
"""
18.5 nsec

python -m timeit "a,b,c,d,e,f,g,h = 1,2,3,4,5,6,7,8"
18.4 nsec

The second version was faster in Python 2 (by around 20%), but it's not longer faster in Python 3.10.4
"""
