date = input("Enter birthday ddmmyyyy: ")

while len(date) > 1:
    temp = 0
    value = str(sum([int(digit) for digit in date]))
    date = value

print(f"Your digit of life is - {date}")

