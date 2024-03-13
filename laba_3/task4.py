def count_string_repeats(strings):
    repeats_dict = {}

    # Подсчет повторений строк и сохранение в словаре
    for string in strings:
        if string in repeats_dict:
            repeats_dict[string] += 1
        else:
            repeats_dict[string] = 1

    # Вывод результатов
    for key in repeats_dict:
        print(repeats_dict[key], end=" ")

# Примеры работы программы
input1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
input2 = ['aaa', 'bbb', 'ccc']
input3 = ['abc', 'abc', 'abc']

print("Выходные данные для входных данных 1:")
count_string_repeats(input1)

print("\nВыходные данные для входных данных 2:")
count_string_repeats(input2)

print("\nВыходные данные для входных данных 3:")
count_string_repeats(input3)
