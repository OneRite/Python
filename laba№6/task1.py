# Чтение матрицы из файла
matrix = []
with open("/Users/ruslan/Documents/GitHub/Python/laba№6/matrix.txt") as file:
    for line in file:
        row = list(map(int, line.strip().split(',')))
        matrix.append(row)

# Нахождение суммы всех элементов
total_sum = sum(sum(row) for row in matrix)

# Нахождение максимального и минимального элементов
flat_matrix = [item for sublist in matrix for item in sublist]
max_element = max(flat_matrix)
min_element = min(flat_matrix)

print("Сумма всех элементов матрицы:", total_sum)
print("Максимальный элемент матрицы:", max_element)
print("Минимальный элемент матрицы:", min_element)