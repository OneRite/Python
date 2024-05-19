import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Создание массива значений x от -1 до 1
x = np.linspace(-1, 1, 500)

# Построение графиков полиномов Лежандра
plt.figure(figsize=(10, 6))
colors = plt.cm.viridis(np.linspace(0, 1, 7))

for n in range(1, 8):
    Pn = legendre(n)  # Получение полинома Лежандра степени n
    y = Pn(x)  # Вычисление значений полинома в точках x
    plt.plot(x, y, label=f'$n = {n}$', color=colors[n-1])

# Настройка графика
plt.title('Полиномы Лежандра')
plt.xlabel('x')
plt.ylabel('P_n(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend(loc='upper right')

# Показ графика
print("Запущено окно")
plt.show()
