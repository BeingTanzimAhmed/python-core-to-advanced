from functools import reduce # Always Import reduce func() before using it



numbers = [1, 2, 3, 4, 67, 6]

def sum(a, b):
    return a + b

c = reduce(sum, numbers)
print(c)