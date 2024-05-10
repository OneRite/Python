import numpy as np

# Заданный вектор
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

# Индексы нулевых элементов
zero_indices = np.where(x == 0)[0]

# Индексы элементов, перед которыми стоит ноль
indices_before_zero = zero_indices - 1

# Отфильтровываем отрицательные индексы
valid_indices = indices_before_zero[indices_before_zero >= 0]

if len(valid_indices) > 0:
    # Находим максимальный элемент
    max_element = np.max(x[valid_indices])
    print("Максимальный элемент среди элементов, перед которыми стоит ноль:", max_element)
else:
    print("В векторе нет элементов, перед которыми стоит ноль.")
