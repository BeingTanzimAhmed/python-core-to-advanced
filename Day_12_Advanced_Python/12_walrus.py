def very_slow_func():
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    return 50

if ((a:= very_slow_func())> 40):
    print(a)
else:
    print("Error")

while (data := input("Enter a value (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {data}")