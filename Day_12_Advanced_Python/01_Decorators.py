'''
A decorator is simply a callable (usually a function) that takes another function as an argument and returns a replacement function. 
The replacement function typically extends or alters the behavior of the original function.
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#f = my_decorator(say_hello)
#f()

