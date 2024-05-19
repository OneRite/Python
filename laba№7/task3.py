import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Функция для генерации фигуры Лиссажу
def lissajous_curve(a, b, delta, t):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y

# Параметры для анимации
delta = 0  # Нулевой сдвиг фаз
t = np.linspace(0, 2 * np.pi, 1000)

# Создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
line, = ax.plot([], [], lw=2)

# Инициализация функции
def init():
    line.set_data([], [])
    return line,

# Функция анимации
def animate(i):
    a = i / 100
    b = 1
    x, y = lissajous_curve(a, b, delta, t)
    line.set_data(x, y)
    return line,

# Создание анимации
anim = FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Отображение анимации
print("Запущено окно")
plt.show()
