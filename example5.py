# example5.py
import numpy  # pip install numpy

def compute_sum_of_powers():
    numbers = numpy.arange(1_000_001)
    powers = numpy.power(numbers, 2)
    return numpy.sum(powers)

total = compute_sum_of_powers()
print(total)
