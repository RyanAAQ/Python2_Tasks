number = input("Enter a number: ")
sums = 0

for digits in number:
    if digits == '1' or digits == '3' or digits == '5' or digits == '7' or digits == '7':
        digits = int(digits)
        sums += digits
        
print(f"The sum of the odd numbers = {sums}")



