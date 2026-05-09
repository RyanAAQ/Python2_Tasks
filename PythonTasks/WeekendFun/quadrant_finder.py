#Collect two numbers

#use conditionals to check if the numbers meet the requirements

#print results based on conditions

number_one = int(input("Enter X: "))
number_two = int(input("Enter Y: "))

if((number_one > 0) and (number_two > 0)):
    print("Q1")
    
elif((number_one < 0) and (number_two > 0)):
    print("Q2")
    
elif((number_one < 0) and (number_two < 0)):
    print("Q3")
    
elif((number_one > 0) and (number_two < 0)):
    print("Q4")
    
elif((number_one == 0) and (number_two == 0)):
    print("Origin")
    
elif((number_one != 0) and (number_two == 0)):
    print("X-axis")

elif((number_one == 0) and (number_two != 0)):
    print("Y-axis")
    
else:
    print("Invalid input")
