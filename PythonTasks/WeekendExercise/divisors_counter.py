number = int(input("Enter a number: "))
count = 0

for numbers in range(1, number + 1):
    if number % numbers == 0:
        count += 1
        
print(f"The number of divisors = {count}")
