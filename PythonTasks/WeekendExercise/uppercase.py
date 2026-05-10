word = input("Enter a word: ")
count = 0

for letters in word:
    if letters.isupper():
        count += 1
    
print(f"The word has {count} uppercase letters")
