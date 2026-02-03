def sum(*args): # Args will be tuples of all the values passed to sum
    total = 0
    for items in args:
        total += items
    return total

print(sum(1,3,4,5,5,2))

def mul(*args): # Args will be tuples of all the values passed to sum
    total = 1
    for items in args:
        total *= items
    return total

print(mul(1,3,4,5,5,2))

def div(*args): # Args will be tuples of all the values passed to sum
    total = 1
    for items in args:
        total /= items
    return total

print(div(50,24,87))

def sub(*args): # Args will be tuples of all the values passed to sum
    total = 1
    for items in args:
        total = total - items
    return total

print(sub(78,1))