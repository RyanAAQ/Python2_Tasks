#Collect the letter

#Check if the letter is a single character

#if the condition is met Check if the letter is a vowel using the for/in loop

#print result based on the condition

letter = input("Enter anny letter: ").lower()

if len(letter) == 1:
    if letter in "aeiou":
        print(f"{letter} is a vowel")
        
    else:
        print(f"{letter} is a consonant")
        
else:
    print("Invalid input")
