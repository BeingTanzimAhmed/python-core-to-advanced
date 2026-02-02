class Employee:

    def __init__(self, salary, name, contract):

        self.salary = salary # An instance attribute is created of name 'Salary' and assign it with salary
        self.name = name
        self.contract = contract

    def get_salary(self): # self is imp. here because it gets allocated to the object which is being created and calling the class
        return self.salary
    
    def get_info(self): # Method created for class employee
        return (f"The name of Employee is {self.name} and Salary is {self.salary} with a contract of {self.contract} in years")
    
E1 = Employee(35000, "Tanzim", 2)

print(E1.get_info())