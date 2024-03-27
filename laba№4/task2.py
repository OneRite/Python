def is_subset(set1, set2):
    return set1.issubset(set2)

# Ввод данных от пользователя
set1_input = input("Введите первое множество чисел через запятую и без пробелов: ")
set2_input = input("Введите второе множество чисел через запятую и без пробелов: ")

# Преобразование ввода в множества чисел
set1 = set(map(int, set1_input.split(',')))
set2 = set(map(int, set2_input.split(',')))

# Проверка и вывод результата
print("Входные данные:", set1, "и", set2)
print("Выходные значения:", is_subset(set1, set2))
