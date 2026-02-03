class Employee:
    def __init__(self, name, salary): #__init__ is a magic method. Please check notes Handbook.
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and salary is {self.salary}." #Dunder method in action. Please refer Handbook notes
    
    def __repr__(self):
        return f"name : {self.name} \nsalary: {self.salary}." #Dunder method in action. Please refer Handbook notes
    
    def __len__(self):
        return len(self.name) #Dunder method in action. Please refer Handbook notes Dunder stands for __ [Double underscore]

e = Employee("Tanzim", 2300000)
# print(e.name, e.salary)
# print(str(e)) #Tycepasting invokes strings
# print(repr(e)) #Tycepasting invokes repr (Mostly used by developers to debug)
print(len(e))