#Write to a file called John Doe.txt.
# It should contain info regarding John Doe's age and country.

f = open("John_Doe.txt", "w")

string = "John Doe is 30 years old. \nHe lives in the USA."

f.write(string)

f.close()

# Read the file to verify its contents
f = open("John_Doe.txt", "r")

content = f.read()

print(content)

f.close()