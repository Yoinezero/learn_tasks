sudoku = []
square1, square2, square3 = 0, 0, 0
valid: bool = True
# input random 9x9 grid with values 1..9
print("Enter sudoku board (9x9): ")
for i in range(9):
    sudoku.append(input())

for line in sudoku:
    if sum([int(el) for el in line]) != 45:
        valid = False

if not valid:
    print("No")
else:
    square1 = sum([int(d) for d in "".join([el[:3] for el in sudoku[:3]])]) == 45
    square2 = sum([int(d) for d in "".join([el[:3] for el in sudoku[3:6]])]) == 45
    square3 = sum([int(d) for d in "".join([el[:3] for el in sudoku[6:]])]) == 45

print("No" if False in (square1, square2, square3) else "Yes")
