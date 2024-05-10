import numpy as np

def run_length_encoding(x):
    # Инициализация пустых списков для хранения уникальных элементов и их количества
    unique_values = []
    counts = []

    # Инициализация переменных для хранения текущего элемента и его количества
    current_value = x[0]
    current_count = 1

    # Проход по элементам вектора начиная со второго элемента
    for i in range(1, len(x)):
        # Если текущий элемент равен предыдущему, увеличиваем счетчик
        if x[i] == current_value:
            current_count += 1
        # Если текущий элемент отличается от предыдущего, добавляем предыдущий элемент и его количество в соответствующие списки
        else:
            unique_values.append(current_value)
            counts.append(current_count)
            # Обновляем текущий элемент и его количество
            current_value = x[i]
            current_count = 1

    # Добавляем последний элемент и его количество в списки
    unique_values.append(current_value)
    counts.append(current_count)

    # Преобразуем списки в массивы NumPy
    unique_values_array = np.array(unique_values)
    counts_array = np.array(counts)

    return unique_values_array, counts_array

# Пример использования функции
x = np.array([2, 2, 2, 3, 3, 3, 5])
result = run_length_encoding(x)
print(result)
