from os import strerror

import matplotlib.pyplot as plt

name = input("Enter file name to use: ") + ".txt"
file = None
out_file = None

try:
    file = open(name, "r")
except IOError as e:
    print("No such file or directory!")
    print(strerror(e.errno))
    exit(e.errno)

letters_count = {}

for line in file:
    for char in line.lower().rstrip('\n'):
        if char.isalpha():
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1

group_data = list(map(lambda x: x[1], sorted(letters_count.items(), key=lambda x: x[1])))
group_names = list(map(lambda x: x[0], sorted(letters_count.items(), key=lambda x: x[1])))

y_pos = range(len(group_names))
fig, ax = plt.subplots()
ax.barh(y_pos, group_data, align="center")
ax.set_yticks(y_pos)
ax.set_yticklabels(group_names)
# ax.invert_yaxis()
ax.set_xlabel('Count')
ax.set_title(f'Letters hist {name}')
plt.savefig(fname=f"{name.rstrip('.txt')}.hist.jpg")
plt.show()

try:
    out_file = open(name.rstrip(".txt") + ".hist.txt", "w")
except IOError as e:
    print("No such file or directory!")
    print(strerror(e.errno))
    exit(e.errno)

for letter, count in sorted(letters_count.items(), key=lambda x: x[1], reverse=True):
    out_file.write(f"{letter} -> {count}\n")

out_file.close()
file.close()
