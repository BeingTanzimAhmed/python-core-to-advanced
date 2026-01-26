num = int(input("Enter the num"))

for i in range(1, 12): # range() func. works between n to n-1 i.e. It will run till 11 for this case.
    print(num, "x ",i,"=", int(i) * num)