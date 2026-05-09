total_bill = int(input("Enter the total bill: "))
is_member = input("Are you a member (Yes or No): ").lower()

if((total_bill >= 1000) and (is_member == "yes")):
    discount = total_bill * (10 / 100)
    final_amount = total_bill - discount
    print(f"With a 10% discount, the final price = ${final_amount}")
    
elif((total_bill >= 1000) and (is_member == "no")):
    discount = total_bill * (5 / 100)
    final_amount = total_bill - discount
    print(f"With a 5% discount, the final price = ${final_amount}")
    
else:
    final_amount = total_bill
    print(f"No discount applied, final price = ${final_amount}")
