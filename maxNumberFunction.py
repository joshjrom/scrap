def findMax(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    
    return max


numbers = input("Enter a list element separated by space: ").split()


print(findMax(numbers))

