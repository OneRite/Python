import numpy as np

# URL для загрузки данных
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Загрузка данных
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Получение столбца 'species'
species_column = iris[:, 4]

# Нахождение уникальных значений и их количества
unique_values, counts = np.unique(species_column, return_counts=True)

# Вывод результатов
print("Уникальные значения в столбце 'species':", unique_values)
print("Количество каждого уникального значения:")
for value, count in zip(unique_values, counts):
    print(value.decode('utf-8'), ":", count)
