# A list containing a table of 6

a = 4
table = []

for i in range(1,12):
    table.append(a*i)

print(table) # Long way

t = [3 * i for i in range(1,12)] #List comprehension way of doing things
print(t)

squared = [x**2 for x in range(1,6)]
print(squared)  # Output: [0, 1, 4, 9, 16]