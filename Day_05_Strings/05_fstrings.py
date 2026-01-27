#String Formatting

template = "Dear {}, You can do it so take this {}$"

a = "Tanzim"
a1 = "10000"
b = "Amman"
b1 = "1000"

s = template.format(a,a1)
print(s) # This is anold way of doing things

# New way is
print(f"Dear {b}, You can do it so take this {b1}$") #f-strings now we should use this

'''
Important Notes

-Escape Sequences: Use \n, \t, \', \", and \\ to handle special characters in strings.
-Raw Strings: Use r"string" to prevent escape sequence interpretation.
-String Encoding & Decoding: Use .encode() and .decode() to work with different text encodings.
-String Immutability: Strings in Python are immutable, meaning they cannot be changed after creation.
-Performance Considerations: Using ''.join(list_of_strings) is more efficient than concatenation in loops.

Summary

-Python provides various string methods for modification and analysis.
-Case conversion, trimming, finding, replacing, splitting, and joining are commonly used.
-Functions like len(), ord(), and chr() are useful for working with string properties.
-.format() allows inserting values into placeholders.
-f-strings provide an intuitive and readable way to format strings.
-f-strings support expressions, calculations, and formatting options.
'''