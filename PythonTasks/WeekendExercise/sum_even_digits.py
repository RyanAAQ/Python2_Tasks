number = input("Enter a number: ")
sums = 0

for digits in number:
    if digits == '2' or digits == '4' or digits == '6' or digits == '8':
        digits = int(digits)
        sums += digits
        
print(f"The sum of the even numbers = {sums}")



