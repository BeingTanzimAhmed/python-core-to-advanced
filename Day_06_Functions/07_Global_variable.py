def sum(a, b):
    print("Hey!, I am summing")
    c = a + b
    global z # Global variable value can be changed when we use global keyword inside the function to change it's value
    z = 0 # This will be referred to Global z and local variable is not created
    return c

z = 81 # Global Variable
print(sum(76, 82))
print(z)