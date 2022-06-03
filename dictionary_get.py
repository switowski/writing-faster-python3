"""
Getting value from a dictionary

python -m timeit -s "D = {number: number*number for number in range(1_000_000)}" "D.get(123213)"
31.9 nsec
python -m timeit -s "D = {number: number*number for number in range(1_000_000)}" "D[123213]"
20.6 nsec (31.9/20.6 = 1.55)

If the key is not in the dictionary, the "slow" way will return None but the "fast" way will throw a KeyError.
The "fast" way is a good method if you know for sure that the key will always be there.
Choosing one way over the other expresses our intentions.
"""

# Setup
D = {number: number*number for number in range(1_000_000)}

# "Fast" way
D[123123]

# "Slow" way
D.get(123213)
