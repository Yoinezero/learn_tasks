word = input("Enter hidden word: ").lower()
sentence = input("Enter character combination: ").lower()

find: bool = True
start_pos = 0

for char in word:
    pos = sentence.find(char, start_pos)
    if pos < 0:
        find = False
        break
    start_pos = pos + 1
print("Yes" if find else "No")

