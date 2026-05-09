count = 0
for number in range(1, 16):
    score = int(input(f"Enter the score of student {number}: "))
    if score >= 45:
        count = count + 1
            
            
print(f"The number of student that passed are {count}")
