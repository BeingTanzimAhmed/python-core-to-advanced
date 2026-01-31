my_set = {1, 2, 3, 4}

my_set.add(5)        # {1, 2, 3, 4, 5}
my_set.remove(2)     # {1, 3, 4, 5}
my_set.discard(10)   # No error if element not found
my_set.pop()         # Removes random element
print(my_set)