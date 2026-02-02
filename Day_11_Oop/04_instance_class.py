class Employee:
    company = "Jaguar" # A class attribute is created here

    def __init__(self, salary, name, contract, company):

        self.salary = salary # An instance attribute is created of name 'Salary' and assign it with salary
        self.name = name
        self.contract = contract
        self.company = company

    def get_salary(self): # self is imp. here because it gets allocated to the object which is being created and calling the class
        return self.salary
    
    def get_info(self): # Method created for class employee
        return (f"The name of Employee is {self.name} and Salary is {self.salary} with a contract of {self.contract} in years and in the company {self.company}")
    
E = Employee(55000, "Tanzim", 2, "Range Rover") 

print(E.get_info()) # An instance attribute is always printed if it's present over Class attribute
print(E.company)
print(Employee.company) # This will always print class attribute

# Object introspection : It's a way to find all the attributes and methods present in a particular objects in python has.
print(dir(E))