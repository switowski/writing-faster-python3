# example6.py

def formula(n):
    return n * (n + 1) * (2 * n + 1) / 6

total = formula(1_000_000)
print(total)
