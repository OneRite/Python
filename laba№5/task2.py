with open("/Users/ruslan/Documents/GitHub/Python/laba№5/input.txt", "r") as file:
    # Считываем строки из файла, разбиваем каждую строку на числа и сохраняем их в список
    numbers = [int(num) for line in file for num in line.strip().split()]

# Сортируем числа по возрастанию
numbers.sort()

# Записываем отсортированные числа в другой файл
with open("/Users/ruslan/Documents/GitHub/Python/laba№5/output.txt", "w") as file:
    # Записываем каждое число на отдельной строке
    for num in numbers:
        file.write(str(num) + "\n")

