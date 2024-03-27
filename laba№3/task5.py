def linearly_dependent(matrix):

    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        print("Матрица должна быть размером 3x3.")
        return

    # Преобразуем матрицу к ступенчатому виду методом Гаусса-Жордана
    for i in range(3):
        if matrix[i][i] == 0:
            # Если на главной диагонали есть нулевой элемент, меняем строки
            for j in range(i + 1, 3):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                continue

        for j in range(i + 1, 3):
            coeff = -matrix[j][i] / matrix[i][i]
            for k in range(3):
                matrix[j][k] += coeff * matrix[i][k]

    # Проверяем последнюю строку (она должна быть нулевой)
    if all(elem == 0 for elem in matrix[2]):
        print("Столбцы матрицы линейно зависимы.")
    else:
        print("Столбцы матрицы линейно независимы.")

# Пример матрицы
mat = [
    [10, 10, 10],
    [10, 70, 70],
    [70, 80, 80]
]

# Вывод матрицы
print("Матрица:")
for row in mat:
    print(row)

# Проверка линейной зависимости столбцов
linearly_dependent(mat)
