import argparse

parser = argparse.ArgumentParser(description = "Simple Calculator")

parser.add_argument("num1", type = float, help = "First number")
parser.add_argument("num2", type = float, help = "Second number")
parser.add_argument("operation", type = str, choices = ["add", "subtract", "multiply", "divide"], help = "Operation to perform")

args = parser.parse_args()

if (args.operation == "add"):
    print (f"The result is: {args.num1 + args.num2}")
elif (args.operation == "subtract"):
    print (f"The result is: {args.num1 - args.num2}")
elif (args.operation == "multiply"):
    print (f"The result is: {args.num1 * args.num2}")
elif (args.operation == "divide"):
    if args.num2 != 0:
        print (f"The result is: {args.num1 / args.num2}")
    else:
        print ("Error: Division by zero is not allowed.")

else:
    print ("Invalid operation.")