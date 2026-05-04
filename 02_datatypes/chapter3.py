# Integers

black_tea_gram = 100
milk_gram = 500
hitesh = "Hitesh"
total_gram = black_tea_gram + milk_gram
print(total_gram)
print("id of black_tea_gram:", id(black_tea_gram))
print("id of milk_gram:", id(milk_gram))
print("id of hitesh:", id(hitesh))

print(type(black_tea_gram))
print(type(milk_gram))  
print(type(hitesh))

# Floats
pi = 3.14
print(pi)
print(type(pi))

# Strings
greeting = "Hello, World!"
print(greeting)
print(type(greeting))


        # Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))

# Tuples
coordinates = (10.0, 20.0)
print(coordinates)
print(type(coordinates))

# Sets
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
print(type(unique_numbers))

# Dictionaries
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
print(type(person))

 # Boolean
is_raining = True
print(is_raining)
print(type(is_raining))

# NoneType
nothing = None
print(nothing)
print(type(nothing))

# Complex Numbers
complex_number = 2 + 3j
print(complex_number)


    # Bytes
byte_data = b"Hello"
print(byte_data)
print(type(byte_data))

# Bytearray
mutable_byte_data = bytearray(b"Hello")
print(mutable_byte_data)
print(type(mutable_byte_data))

# Frozenset
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)
print(type(frozen_set)) 

# Range
number_range = range(1, 10)
print(number_range)
print(type(number_range))
 # Memoryview
memory_view = memoryview(b"Hello")
print(memory_view)
print(type(memory_view))

# NoneType
none_value = None
print(none_value)

# Type Conversion
number_str = "123"
number_int = int(number_str)
print(number_int)
number_float = float(number_str)
print(number_float)
number_str_again = str(number_int)
print(number_str_again)

# Type Checking
print(isinstance(number_int, int))
print(isinstance(number_float, float))      
print(isinstance(greeting, str))

# Type Casting
print(float(10))
print(int(3.14))


# String Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# List Operations
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.remove(3)
print(numbers)

# Dictionary Operations
person["age"] = 31
print(person)

# Set Operations
unique_numbers.add(6)
print(unique_numbers)
unique_numbers.remove(2)
print(unique_numbers)

# Tuple Operations
coordinates = (10.0, 20.0)
print(coordinates[0])  # Accessing tuple elements

# Range Operations
number_range = range(1, 10)
print(number_range[0])  # Accessing range elements

# Memoryview Operations
memory_view = memoryview(b"Hello")
print(memory_view[0])  # Accessing memoryview elements

# Frozenset Operations
frozen_set = frozenset([1, 2, 3, 4, 5])
print(3 in frozen_set)  # Checking membership in frozenset

#   Bytes Operations

byte_data = b"Hello"
print(byte_data[0])  # Accessing byte data elements     

# Bytearray Operations
mutable_byte_data = bytearray(b"Hello")
print(mutable_byte_data[0])  # Accessing bytearray elements

# Boolean Operations
is_raining = True
print(is_raining and False)  # Logical AND
print(is_raining or False)   # Logical OR
print(not is_raining)        # Logical NOT

# NoneType Operations
none_value = None
print(none_value is None)  # Checking if value is None

# Complex Number Operations
complex_number1 = 2 + 3j
complex_number2 = 1 + 4j
print(complex_number1 + complex_number2)  # Addition of complex numbers
print(complex_number1 * complex_number2)  # Multiplication of complex numbers

# Type Annotations
def add_numbers(a: int, b: int) -> int:
    return a + b
result = add_numbers(5, 10)
print(result)
