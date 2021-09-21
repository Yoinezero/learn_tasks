from random import randrange
import os


def display_board(board):
    os.system('cls||clear')
    plus_horizontal = (0, 8, 16, 24)
    plus_vertical = (0, 4, 8, 12)
    coordinates = {(2, 4): (0, 0), (2, 12): (0, 1), (2, 20): (0, 2),
                   (6, 4): (1, 0), (6, 12): (1, 1), (6, 20): (1, 2),
                   (10, 4): (2, 0), (10, 12): (2, 1), (10, 20): (2, 2)}

    for i in range(13):
        for j in range(25):
            if (i, j) in coordinates:
                tup = coordinates.get((i, j))
                print(board[tup[0]][tup[1]], end='')
                del tup
                continue
            if j in plus_horizontal and i in plus_vertical:
                print('+', end='')
            elif j not in plus_horizontal and i in plus_vertical:
                print('-', end='')
            elif j in plus_horizontal and i not in plus_vertical:
                print('|', end='')
            elif j not in plus_horizontal and i not in plus_vertical:
                print(" ", end='')
        print()


def enter_move(board):
    get_free_moves = make_list_of_free_fields(board)
    coordinates = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                   4: (1, 0), 5: (1, 1), 6: (1, 2),
                   7: (2, 0), 8: (2, 1), 9: (2, 2)}
    pos = input("Enter free position you want to use: ")
    while pos not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        pos = input("Wrong value, position is not exist, try again: ")
    pos = int(pos)
    tup = coordinates.get(pos)
    while get_free_moves[pos - 1] == '-':
        pos = int(input("Wrong value, position is not free, try again: "))
        tup = coordinates.get(pos)
    else:
        board[tup[0]][tup[1]] = 'X'
    display_board(board)


def make_list_of_free_fields(board):
    free = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in ('O', 'X'):
                free.append((i, j))
            else:
                free.append('-')
    return free


def victory_for(board):
    for i in range(len(board)):
        if board[i] == ['O', 'O', 'O']:
            return 1
        elif board[i] == ['X', 'X', 'X']:
            return 2

    a1, a2, a3 = [], [], []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 0:
                a1.append(board[i][j])
            elif j == 1:
                a2.append(board[i][j])
            else:
                a3.append(board[i][j])

    a = [a1, a2, a3]

    for el in a:
        if el == ['O', 'O', 'O']:
            return 1
        elif el == ['X', 'X', 'X']:
            return 2

    d1 = [board[0][0], board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]
    if d1 == ['O', 'O', 'O'] or d2 == ['O', 'O', 'O']:
        return 1
    elif d1 == ['X', 'X', 'X'] or d2 == ['X', 'X', 'X']:
        return 2

    free = make_list_of_free_fields(board)

    if free.count('-') == 9:
        return 0

    return -1


def draw_move(board):
    get_free_moves = make_list_of_free_fields(board)
    if get_free_moves.count('-') == 9:
        return
    coordinates = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                   4: (1, 0), 5: (1, 1), 6: (1, 2),
                   7: (2, 0), 8: (2, 1), 9: (2, 2)}
    pos = randrange(1, 10)
    tup = coordinates.get(pos)
    while get_free_moves[pos - 1] == '-':
        pos = randrange(1, 10)
        tup = coordinates.get(pos)
    else:
        board[tup[0]][tup[1]] = 'O'
    display_board(board)


continue_answer = True
while continue_answer:
    continue_answer = False
    bord = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    val = -1
    display_board(bord)
    while True:
        enter_move(bord)
        val = victory_for(bord)
        if val == 1:
            print("You lose!")
            break
        elif val == 2:
            print("You win!")
            break
        elif val == 0:
            print("Draw!")
            break
        draw_move(bord)
        val = victory_for(bord)
        if val == 1:
            print("You lose!")
            break
        elif val == 2:
            print("You win!")
            break
        elif val == 0:
            print("Draw!")
            break

    ans = str(input("Do you want to continue? [Y, n] "))
    if ans in ("Y", "y", ""):
        continue_answer = True
    else:
        continue_answer = False

input("Press any key to exit...")
