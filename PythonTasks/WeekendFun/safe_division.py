#Collect X and Y

#Check if y = 0

#Calculate the result if Y is not = 0

#print result

number_one = int(input("Enter X: "))
number_two = int(input("Enter Y: "))

if (number_two != 0):
    result = number_one / number_two
    print(f"The result = {result}")
    
else:
    print("Cannot divide by zero")
