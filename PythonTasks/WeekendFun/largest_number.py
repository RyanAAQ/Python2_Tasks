#Collect three numbers 

#set the largest as the first number

#compare the numbers to see which is larger

#print the largest

number_one = int(input("Enter a: "))
number_two = int(input("Enter b: "))
number_three = int(input("Enter c: "))

largest = number_one

if number_two > largest:
    largest = number_two

if number_three > largest:
    largest = number_three

print(f"The largest number is {largest}")

