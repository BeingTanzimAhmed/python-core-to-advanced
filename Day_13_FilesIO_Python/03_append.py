# Append to an existing file called John_Doe.txt.
# It should add info regarding John Doe's profession.

f = open("John_Doe.txt", "a")

string = " \nHe is a software engineer."

f.write(string)

f.close()

# Read the file to verify its contents
f = open("John_Doe.txt", "r")

content = f.read()

print(content)

f.close()