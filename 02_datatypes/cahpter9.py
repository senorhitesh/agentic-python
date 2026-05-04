# # Dictionaries
# # A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

# # Creating a dictionary
# my_dict = {
#     "age": 30,
#     "name": "Alice",
#     "city": "New York"
# }
# # Accessing values
# print(my_dict["name"])  # Output: Alice
# print(my_dict["age"])   # Output: 30

# # Adding a new key-value pair
# my_dict["country"] = "USA"
# # Updating an existing value
# my_dict["age"] = 31
# # Removing a key-value pair
# del my_dict["city"]
# # Iterating through a dictionary
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# # Output:
# # name: Alice
# # age: 31
# # Checking if a key exists
# if "name" in my_dict:
#     print("Name is in the dictionary.")
# # Output: Name is in the dictionary.


# # Dictionary methods
# # Get a value with a default if the key does not exist
# print(my_dict.get("city", "Not found"))  # Output: Not found
# # Get all keys
# print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
# # Get all values
# print(my_dict.values())  # Output: dict_values(['Alice', 31, 'USA'])
# # Get all key-value pairs
# print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')])



chai_order  = dict(type="chai", size="medium", price=3.5)
print(chai_order)  # Output: {'type': 'chai', 'size': 'medium', 'price': 3.5}