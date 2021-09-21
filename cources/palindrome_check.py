string = input("Enter: ").lower().replace(" ", "")

print("It's a palindrome") if string == string[::-1] else print("Oh no!")

input("Press any key to exit...")
