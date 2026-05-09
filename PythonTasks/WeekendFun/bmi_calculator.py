#Collect the weight and height

#Calculate for the bmi

#use the result in conditionals

#print the result based on the conditionals

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

if (bmi < 18.5):
    print("Underweight")
    
elif ((bmi >= 18.5) and (bmi <= 24.9)):
    print("Normal")
    
elif ((bmi >= 25) and (bmi <= 29.9)):
    print("Overweight")
    
else:
    print("Obese")

