# Set
# Sets are unordered collections of unique elements. They are mutable, meaning you can add or remove elements from a set after it has been created. Sets are defined using curly braces {} or the built-in set() function.

#example

# Creating a set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
all_set = set1.union(set2)  # Union of two sets
all_set = set1 | set2  # Union of two sets

intersection_set = set1.intersection(set2)  # Intersection of two sets
print("Set 1:", set1)

print(2 in set1)  # Check if an element is in the set
print(6 in set1)  # Check if an element is in the set
