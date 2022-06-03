# example3.py

def compute_sum_of_powers():
    return sum([n * n for n in range(1_000_000)])

total = compute_sum_of_powers()
print(total)
