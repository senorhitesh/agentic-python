text = "education"

vowels = [ch for ch in text if ch.lower() in "aeiou"]

print(vowels)

array = [[1, 2], [3, 4], [5, 6]]

flatten = [item for sublist in array for item in sublist]

print(flatten)

for num in range(2, 101):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)


matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transpose = []

for col in range(len(matrix[0])):
    row = []

    for r in matrix:
        print(r)
        row.append(r[col])

    transpose.append(row)

print(transpose)

