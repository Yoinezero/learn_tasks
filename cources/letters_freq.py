from os import strerror

name = input("Enter file name: ")
letters_n_count = {}

try:
    file = open(name, "r")
except IOError as e:
    print(f"File don't found {strerror(e.errno)}")
    exit(e.errno)

try:
    read = file.readline().lower()
    while read:
        for ch in read:
            if ch in letters_n_count:
                letters_n_count[ch] += 1
            else:
                letters_n_count[ch] = 1
        read = file.readline().lower()
except IOError as e:
    print(f"Error occurred {strerror(e.errno)}")
    exit(e.errno)
else:
    print("well done, here is Histogram")

