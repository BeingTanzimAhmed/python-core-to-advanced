'''
Classes and Objects: The Blueprint and the Building

Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.

Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.

'''
class Employee:
    company = "HP"

    def get_salary(self): # self is imp. here because it gets allocated to the object which is being created and calling the class
        return 30000
    
e = Employee() # An object of class Employee is created 
print(e.get_salary()) # Employee e's get_salary method is called
print(e.company)
