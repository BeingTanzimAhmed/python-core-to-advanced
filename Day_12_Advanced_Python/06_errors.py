# while True : 
#     try:
        
#         a = float(input("Enter first number: "))
#         b = float(input("Enter second number: "))
#         print(f"The division is: {a / b}")
    
#     except ZeroDivisionError:
#         print("Please dont divide by 0")
#     except ValueError:
#         print("Please enter float or integers only")
#     except Exception as e:
#         print("Unknown error occured", e)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if b ==0:
    raise ValueError("Please don't divide by zero")

print(f"The division is: {a / b}")
