letter = input("Enter anny letter: ").lower()

if len(letter) == 1:
    if letter in "aeiou":
        print(f"{letter} is a vowel")
        
    else:
        print(f"{letter} is a consonant")
        
else:
    print("Invalid input")
