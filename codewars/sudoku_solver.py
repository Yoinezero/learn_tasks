puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


class Sudoku:
    def __init__(self, matrix: list[list]):
        self.grid = matrix
        # self.mask = [[(1 if d else 0) for d in line] for line in matrix]

    # @property
    # def masked(self):
    #     return sum(sum(el) for el in self.grid) != 81

    def __check_row(self, row: int, num: int):
        for col in range(9):
            if self.grid[row][col] == num:
                return True
        return False

    def __check_col(self, col: int, num: int):
        for row in range(9):
            if self.grid[row][col] == num:
                return True
        return False

    def __check_sub(self, row: int, col: int, num: int):
        c, r = row // 3, col // 3
        for col in range(3 * c, 3 * (c + 1)):
            for row in range(3 * r, 3 * (r + 1)):
                if self.grid[col][row] == num:
                    return True
        return False

    def check_move(self, row: int, col: int, num: int):
        return not self.__check_col(col, num) and not self.__check_row(row, num) and not self.__check_sub(row, col, num)

    def find_location(self):
        for x in range(9):
            for y in range(9):
                if self.grid[x][y] == 0:
                    return x, y
        return False

    def __str__(self):
        return "\n".join(str(el) for el in self.grid)


def solve(obj: Sudoku):
    # if not obj.masked:
    #     return True
    location = obj.find_location()
    if not location:
        return True
    x, y = location
    for num in range(1, 10):
        if obj.check_move(x, y, num):
            obj.grid[x][y] = num
            # obj.mask[x][y] = 1
            # obj.mask[x][y] = 1

            if solve(obj):
                return True

            obj.grid[x][y] = 0
            # obj.mask[x][y] = 0
    return False


def sudoku(matrix):
    ans = Sudoku(matrix)
    if solve(ans):
        return ans.grid


print(sudoku(puzzle))
