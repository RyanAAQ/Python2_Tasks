age = int(input("Enter your age: "))

if (age < 5):
    print("Free")
    
elif(age <= 12):
    print("Price = $5")
    
elif(age <= 64):
    print("Price = $12")
    
else:
    print("Price = $8")
