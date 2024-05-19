import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Генерация данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.square(x) + np.square(y)  # Пример функции MSE

# Построение первого графика
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis') #цветной рграфик
ax.set_title('MSE')

# Построение второго графика с логарифмическим масштабом по оси Z
ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(x, y, np.log(z + 1), cmap='viridis')  # Добавляем 1, чтобы избежать log(0)
ax.set_title('MSE в логарифмическом масштабе')
ax.set_zscale('log')
print('окно запущено')
plt.show()
