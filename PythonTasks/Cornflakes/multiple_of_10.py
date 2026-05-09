total = 0

for number in range(20001):
    if number % 10 == 0:
        total = number + total
    
print(f"The sum of the multiples of 10 = {total}")
