number = int(input("Enter any number: "))
temp_number = number
reverse = 0

while number > 0:

    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10
    
if reverse == temp_number:
    print(f"{temp_number} is a palindrome")
        
else:
    print(f"{temp_number} is not a palindrome")
        

