# example2.py

def compute_sum_of_powers():
    total = 0
    for x in range(1_000_000):
        total = total + x*x
    return total

total = compute_sum_of_powers()
print(total)
