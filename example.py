# example.py

TOTAL = 0
def compute_sum_of_powers():
    global TOTAL
    for x in range(1_000_000):
        TOTAL = TOTAL + x*x

compute_sum_of_powers()
print(TOTAL)
