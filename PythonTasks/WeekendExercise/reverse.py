word = input("Enter any word: ")
reverse = ""

for character in word:
    reverse = character + reverse

print(reverse)
