numbers = [1, 10, 20, 2, 5]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
unique.sort()
print(unique)