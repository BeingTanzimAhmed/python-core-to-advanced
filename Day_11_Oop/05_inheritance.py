# Inheritance is like a family tree. A child class (or subclass) inherits traits (attributes and methods) from its parent class (or superclass). 
# This allows you to create new classes that are specialized versions of existing classes, without rewriting all the code.




class Animal:  # Parent class (superclass)

    Location = "Kolkata"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self):  # We *override* the speak method (more on this later)
        super().speak() # We are using the speak function of the parent class!
        print("Woof!") # Inheritance in Python works like this

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name)  # Output: Rover
print(my_cat.name)  # Output: Fluffy

# They both have a 'speak' method, but it behaves differently:
my_dog.speak()  # Output: Woof!
my_cat.speak()  # Output: Meow!

# super(): Inside a child class, super() lets you call methods from the parent class. This is useful when you want to extend the parent's behavior instead of completely replacing it. It's especially important when initializing the parent class's part of a child object.