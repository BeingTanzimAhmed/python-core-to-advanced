def repeat(n):
    def decorator(func):
        def wrapper(a):
            for _ in range(n):
                func(a)
        return wrapper
    return decorator
 
@repeat(9)
def greet(name):
    print(f"Hello, {name}!")
 
greet("world")