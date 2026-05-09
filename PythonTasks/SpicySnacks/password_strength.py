#Collect the password

#use the len() to check length of password

#use conditionals to check the password length

password = input("Enter your password: ")

if (len(password) <= 6):
    print("Weak password")
    
elif ((len(password) > 6) and (len(password) <= 10)):
    print("Medium")
    
elif(len(password) > 10):
    print("Strong password")
    
elif(len(password) < 1):
    print("Invalid password")

