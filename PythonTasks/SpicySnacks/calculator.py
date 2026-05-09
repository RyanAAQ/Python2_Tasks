#Collect the two numbers for the calculation

#Collect the operator to be used

#use conditionals to determine the input

#print the result based on the input



print("*" * 66)
print(" SIMPLE CALC ")
print("*" * 66)

firstnumber = int(input("\nEnter First Number: "))
operator = input("Enter operatorerator (+, -, /, //, *, **, %): ").strip()
secondnumber = int(input("Enter Second Number: "))

if operator == "+":
    print(f"Result: {firstnumber + secondnumber}")
elif operator == "-":
    print(f"Result: {firstnumber - secondnumber}")
elif operator == "*":
    print(f"Result: {firstnumber * secondnumber}")
elif operator == "/":
    if secondnumber != 0:
        print(f"Result: {firstnumber / secondnumber}")
    else:
        print("Error: Division by zero")
elif operator == "//":
    if secondnumber != 0:
        print(f"Result: {firstnumber // secondnumber}")
    else:
        print("Error: Division by zero")
elif operator == "**":
    print(f"Result: {firstnumber ** secondnumber}")
elif operator == "%":
    print(f"Result: {firstnumber % secondnumber}")
else:
    print("Invalid operator.")

