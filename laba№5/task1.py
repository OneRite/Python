# Открываем файл для чтения
with open("/Users/ruslan/Documents/GitHub/Python/laba№5/input.txt", "r") as file:
    # Читаем строку из файла и разбиваем её на числа
    numbers = list(map(int, file.readline().split()))

# Вычисляем произведение чисел
product = 1
for num in numbers:
    product *= num

# Открываем файл для записи
with open("/Users/ruslan/Documents/GitHub/Python/laba№5/output.txt", "w") as file:
    # Записываем произведение в файл
    file.write(str(product))