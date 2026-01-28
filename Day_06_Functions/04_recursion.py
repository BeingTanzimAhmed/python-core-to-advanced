def factorial(n):
    # Base case of recursion
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120


def fib(n):
    # Base case of recursion
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)

print(fib(7))
'''
Important Notes:

Must have a base case to avoid infinite recursion.
Used in algorithms like Fibonacci, Tree Traversals.
'''