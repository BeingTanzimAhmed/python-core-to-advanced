name = "tanzim ahmed" #Strings are immutable in nature

#name[0] = "A" can't do this as it's immutable
length = len(name) #len() functions returns length of string
print(length)
print(name.upper(), name)
print(name.capitalize())
print(name.title())

text = "  hello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"

text = "Python is fun and fun"
print(text.find("is"))   # Output: 7 #index of 1st occurence
print(text.replace("fun", "awesome"))  # Output: "Python is awesome and awesome"

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

new_text = " - ".join(fruits)
print(new_text)  # Output: "apple - banana - orange"

print(ord('C'))  # Output: 67
print(chr(68))   # Output: 'D'

text = "Python123"
print(text.isalpha())  # Output: False
print(text.isdigit())  # Output: False
print(text.isalnum())  # Output: True
print(text.isspace())  # Output: False