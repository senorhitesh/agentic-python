# Lists
# Lists are mutable sequences, typically used to store collections of homogeneous items (where the precise degree of similarity will vary by application).
# Lists are defined by having values between square brackets [ ].

# Example of a list
squares = [1, 4, 9, 16, 25]

employees = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}, {"name": "Doe", "age": 35}]

print(list(employees[0].items()))  # Output: [('name', 'John'), ('age', 30)]
print(list(employees[1].items()))  # Output: [('name', 'Jane'), ('age', 25)]
print(list(employees[2].items()))  # Output: [('name', 'Doe'), ('age', 35)]

employees.remove({"name": "John", "age": 30})
print(employees)  # Output: [{'name': 'Jane', 'age': 25 }]
employees.append({"name": "John", "age": 30})
employees.reverse()
print(employees)  


chai = ["chai", "chai2", "chai3", "chai4", "chai5"]
chai.reverse()
print(chai)


sqares = [1, 4, 9, 16, 25]
print(max(sqares))  # Output: 25
print(min(sqares))  # Output: 1
print(sum(sqares))  # Output: 55    
print(len(sqares))  # Output: 5
print(sqares * 4)   # Output: [1, 4, 9, 16, 25, 1, 4, 9, 16, 25, 1, 4, 9, 16, 25, 1, 4, 9, 16, 25]

# why is bytearray not a list? Because it is immutable, and lists are mutable.
# where is bytearray used? It is used for binary data, such as images, audio, and video files. It is also used for network communication, where data is sent in bytes.