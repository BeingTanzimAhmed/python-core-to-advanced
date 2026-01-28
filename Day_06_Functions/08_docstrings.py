def sum(a, b):
    '''This will sum two numbers''' # Docstrings
    c = a + b
    return c
print(sum.__doc__) # way to print docstrings

def add(a, b):
    """
    Returns the sum of two numbers.
 
    Parameters:
    a (int): The first number.
    b (int): The second number.
 
    Returns:
    int: The sum of the two numbers.
    """
    return a + b
print(add.__doc__)

"""
Summary

-Functions help in reusability and modularity.
-Functions can take arguments and return values.
-Lambda functions are short, inline functions.
-Recursion is a technique where a function calls itself.
-Modules help in organizing code and using external libraries.
-Scope and lifetime of variables decide their accessibility.
-Docstrings are used to document functions, classes, and modules.
"""