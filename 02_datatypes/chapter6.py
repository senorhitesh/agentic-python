# Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuples are often used to represent fixed collections of items, such as coordinates (x, y) or database records.

# Example 1: A tuple representing a point in 2D space
point = (3, 4)
print("Point:", point)

# Example 2: A tuple representing a database record
employee = ("John Doe", 30, "Engineer")
index = employee.index("John Doe")  # This will return the index of "John Doe" in the tuple
print("Employee:", employee)
print("Index of John Doe:", index)


masala = ("cumin", "turmeric", "coriander")
(masala1, masala2, masala3) = masala

ginger_ratio, sugar_ratio = 1, 2
print("Ginger Ratio:", ginger_ratio)

# Membership 
# The 'in' keyword is used to check if a value exists in a tuple. It returns True if the value is found, and False otherwise.
print("John Doe in employee:", "John Doe" in employee)
print("Jane Smith in employee:", "Jane Smith" in employee)