class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property #Property Decorator
    def first_name(self):
        return self.name.split(" ")[0] #This (" ") [0] will give First name and [1] will give last name assuming Full name has First and Last Name
    # (.split) simply returns a list

    @first_name.setter
    def first_name(self,  first): # Change first name
        self.name.split(" ")
        new_name = f"{first} {self.name.split(" ")[1]}"
        self.name = new_name

    @property
    def last_name(self):
        return self.name.split(" ")[1]
    
e = Employee(input("Please enter the name: "), int(input ("Please enter the salary amount: ")))
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "Tanzim"
print(e.name)
print(e.salary)
print(e.last_name)
# Setters and getters are used for writing cleaner syntax in Python