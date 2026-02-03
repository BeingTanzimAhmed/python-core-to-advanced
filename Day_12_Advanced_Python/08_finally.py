def divide(a,b):
    try:
        c = a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    # This is always executed if try completely executes or not
    finally:
        print("This is always executed")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

divide(a, b)
