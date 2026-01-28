def sum(a, b):
    c = a + b
    z = 1 # A local variable is created for the function and gets destroyed once the function returns itself.
    return c
    # a, b, c are local variables as they are vanised outside the sum() function. We cannot use or print these variables outside the function.

z = 10 # z is a global variable. We can use it anywhere in the program
print(sum(b = 8, a = 32))
print(z) # Global variable is printed