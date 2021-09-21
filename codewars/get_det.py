def determinant(matrix):
    if len(matrix) == 1: return matrix[0][0]
    x, lng = 0, len(matrix)
    result = 0
    while x != lng:
        if lng > 2:
            det = []
            for i in range(1, lng):
                temp = []

                for j in range(lng):
                    if j == x:
                        continue
                    temp.append(matrix[i][j])

                det.append(temp)

            if (x + 1) % 2 == 0:
                result -= matrix[0][x] * determinant(det)
            else:
                result += matrix[0][x] * determinant(det)
        else:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        x += 1

    return result


print(determinant([[2, 5, 3], [1, -2, -1], [1, 3, 4]]))
