# example4.py

def compute_sum_of_powers():
    return sum(n * n for n in range(1_000_001))

total = compute_sum_of_powers()
print(total)
