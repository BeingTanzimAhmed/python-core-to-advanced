name = "Harry"
print(name [1:-1]) #Same as printing [1:4] works same as range() [n-1]--Output

text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)

text = "Python Programming"
print(text[2::2])   # Output: to rgamn
print(text[:4:2])  # [:4:2] 2 here skips (n-1) character i.e. 2- 1= 1 character is skipped
print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)

'''
Indexing allows accessing individual characters.

Positive indexing starts from 0, negative indexing starts from -1.

Slicing helps extract portions of a string.

The step parameter defines the interval for selection.

Using [::-1] reverses a string.
'''