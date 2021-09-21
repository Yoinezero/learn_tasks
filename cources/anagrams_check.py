first_word = list(input("Enter 1 word: ").lower().replace(" ", ""))
second_word = list(input("Enter 2 word: ").lower().replace(" ", ""))

if str(first_word.sort()) == str(second_word.sort()):
    print("Anagrams")
else:
    print("Not anagrams")
input("Press enter to exit...")
