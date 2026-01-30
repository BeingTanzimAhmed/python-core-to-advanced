a = (3, 4, 1, 6, 9)

print(a[0:2])
print(a[-1])

b = (3, ) # Way to write a single element in tuples
print(b)

a[2] = 2 #Will throw an error as Tuple is im-mutable






'''
Why Use Tuples?

- Faster than lists (since they are immutable)
- Used as dictionary keys (since they are hashable)
- Safe from unintended modifications
'''