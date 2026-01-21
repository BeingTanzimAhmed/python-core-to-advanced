a = int(input("Enter your lucky number between 1 and 10: "))

if(a == 0):
    print("Error!, Out of range")
    
elif(a<10):

    match a:
        case 8:
            print("You got 1$")
        case 5:
            print("You got a free hamper")
        case 1:
            print("Just 2$")
        case _:
            print("Better luck next time")
else:
    print("Please enter in the given range")
print("This is the end")