number = int(input("Enter a number: "))

for numbers in range(1, number + 1):
    if number % numbers == 0:
        print(numbers, end=",")
