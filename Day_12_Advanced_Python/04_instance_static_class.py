class Employee:
    company = "HP" # Class Attributes
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_info(self): # instance method (Default)
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod 

    # Now we don't need to call self and there will be no error
    # if we don't use static decorator then we will need to call self then the error will not be thrown
    # Static method doesn't require self and self is not automatically passed when we call this static func.
    # static method does'nt need instance of the class to run  
    def sum(a, b):
        return a + b
    
    @classmethod #Class methods
    def print_company(cls):
        print(cls.company)

    @classmethod #Class methods
    def change_company(cls, new_company):
         cls.company = new_company 

e1 = Employee("Amman", 2000000)
e2 = Employee("Tanzim", 2000000000)
# print(Employee.company) [Ctrl + / to comment out lines]

# e1.print_info()
# e2.print_info()
# print(e2.sum(3, 4))
print(Employee.company)
e1.change_company("Apple")
# print(e1.print_company())
print(Employee.company)
