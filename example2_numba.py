# example2_numba.py

"""
Alternative step 2
If we can't turn our for loop into a nice list comprehension combined with a built-in function (as you can see in "example3.py"), there is another trick that we can use.
We can use the numba library that is basically a JIT compiler packed as a Python package.
It offers a @jit decorator that we can apply to our function to cut its execution time by half.
Numba works great for math heavy loops.
"""
from numba import jit  # pip install numba

@jit
def compute_sum_of_powers():
    total = 0
    for x in range(1_000_000):
        total = total + x*x
    return total

total = compute_sum_of_powers()
print(total)

# It took 34.4 msec on my computer
# Just like with numpy in example5.py, benchmarks have to run twice to minimize the performance impact of the import statement
# (which shouldn't be part of the benchmark in the first place)
