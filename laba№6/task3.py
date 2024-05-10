import numpy as np

# Генерация массива случайных чисел нормального распределения размера 10x4
array = np.random.normal(size=(10, 4))

# Нахождение минимального значения
min_value = np.min(array)

# Нахождение максимального значения
max_value = np.max(array)

# Нахождение среднего значения
mean_value = np.mean(array)

# Нахождение стандартного отклонения
std_deviation = np.std(array)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = array[:5]

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_deviation)
print("Первые 5 строк:")
print(first_five_rows)
