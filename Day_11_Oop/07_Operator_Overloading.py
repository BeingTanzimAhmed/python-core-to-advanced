class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        #  'other' refers to the object on the *right* side of the +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self): # String representation (for print() and str())
        return f"({self.x}, {self.y})"

    def __eq__(self, other): # Overloading == operator
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2  # This now works!  It calls p1.__add__(p2)
print(p3)      # Output: (4, 6)  (This uses the __str__ method)

print(p1 == p2) # Output: False (This uses the __eq__ method)