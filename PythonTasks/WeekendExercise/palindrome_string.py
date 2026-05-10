word = input("Enter any word: ")
reverse = ""

for character in word:
    reverse = character + reverse
    
if reverse == word:
    print(f"{word} is a palindrome")

else:
    print(f"{word} is not a palindrome")

