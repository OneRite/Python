import numpy as np
import matplotlib.pyplot as plt

# Параметры для фигур Лиссажу
frequency_ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
time = np.linspace(0, 2 * np.pi, 1000)

# Создание подграфиков
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle('Фигуры Лиссажу')

for ax, (a, b) in zip(axs.flat, frequency_ratios):
    x = np.sin(a * time)
    y = np.cos(b * time)
    ax.plot(x, y)
    ax.set_title(f'Соотношение частот: {a}:{b}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
print("Запущено окно")
plt.show()
