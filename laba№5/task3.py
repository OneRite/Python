# Инициализируем переменные для хранения информации о самом старшем и самом младшем ребенке
eldest_child = None
youngest_child = None
max_age = 0
min_age = float('inf')  # Используем бесконечность как начальное значение для возраста

# Открываем файл для чтения
with open("/Users/ruslan/Documents/GitHub/Python/laba№5/дети.txt", "r") as file:
    # Читаем каждую строку из файла
    for line in file:
        # Разбиваем строку на компоненты (фамилия, имя, возраст)
        surname, name, age = line.strip().split()

        # Преобразуем возраст в целое число
        age = int(age)

        # Проверяем, является ли текущий ребенок старше самого старшего
        if age > max_age:
            max_age = age
            eldest_child = f"{surname} {name} {age}"

        # Проверяем, является ли текущий ребенок младше самого младшего
        if age < min_age:
            min_age = age
            youngest_child = f"{surname} {name} {age}"

# Записываем информацию о самом старшем ребенке в файл
with open("/Users/ruslan/Documents/GitHub/Python/laba№5/самый_старший.txt", "w") as file:
    file.write(eldest_child)

# Записываем информацию о самом младшем ребенке в файл
with open("/Users/ruslan/Documents/GitHub/Python/laba№5/самый_младший.txt", "w") as file:
    file.write(youngest_child)
