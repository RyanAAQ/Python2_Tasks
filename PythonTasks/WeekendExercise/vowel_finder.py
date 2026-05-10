word = input("Enter a word: ").lower()

count = 0 

for letter in word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print(count)
        break
    count = count + 1

