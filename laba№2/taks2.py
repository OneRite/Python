value = int(2 ** float(input("Введите число большее 2-х: ")))

triangle = [[0] * value for _ in range(value)]

for i in range(value):
    triangle[i][0] = 1
    triangle[i][i] = 1

for i in range(1, value):
    for j in range(1, i):
        triangle[i][j] = (triangle[i - 1][j - 1] + triangle[i - 1][j]) % 2

for i, row in enumerate(triangle):
    spaces = " " * (value - i - 1)
    print(f"{spaces}{' '.join(['*' if cell == 1 else ' ' for cell in row]).strip()}")
