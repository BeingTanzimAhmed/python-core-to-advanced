def is_greater_than_9(x):
    if x > 9:
        return True
    else:
        return False
    
a = [1, 56, 78, 32, 45, 2, 19]

new = list (filter(is_greater_than_9, a))
print(new)