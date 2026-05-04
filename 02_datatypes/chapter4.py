# String [Immutable]
    #core
    #indexing
    #slicing
    #methods
    #formatting

chai_type = "Green Tea"
customer_name = "Alice"
# Concatenation
greeting = "Hello, " + customer_name + "! Welcome to our tea shop."
# print(greeting , id(customer_name))
# Repetition
echo = "Echo! " * 3
# print(echo)
# Indexing
first_letter = chai_type[0]
# print(first_letter)

# Methods
upper_chai = chai_type.upper()
# print(upper_chai)
# Formatting
formatted_string = f"{customer_name} loves {chai_type}."
# print(formatted_string)

# Slicing

tea_type = chai_type[0:10:2]
print(tea_type)

# Encoding & Decoding
encoded_chai = chai_type.encode('utf-8')
print(encoded_chai)
decoded_chai = encoded_chai.decode('utf-8')
print(decoded_chai)

#why encoding & decoding  used & where it is used
# Encoding is used to convert a string into bytes, which is necessary for storing or transmitting data in a format that can be easily handled by computers. Decoding is the reverse process, where bytes are converted back into a string. This is particularly important when dealing with data that needs to be stored in files, sent over networks, or when working with databases. For example, when you save a text file, the string data is encoded into bytes before being written to the file. When you read the file, the bytes are decoded back into a string for use in your program.

