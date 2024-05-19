import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, VBox, HBox

# Функция для генерации синусоидальной волны
def generate_wave(amplitude, frequency, x):
    return amplitude * np.sin(frequency * x)

# Функция для обновления графиков
def update_plot(amplitude1, frequency1, amplitude2, frequency2):
    x = np.linspace(0, 10, 1000)
    y1 = generate_wave(amplitude1, frequency1, x)
    y2 = generate_wave(amplitude2, frequency2, x)
    y_sum = y1 + y2
    
    ax1.clear()
    ax1.plot(x, y1, label='Wave 1')
    ax1.set_title('Wave 1')
    ax1.set_ylim(-10, 10)
    ax1.legend()
    
    ax2.clear()
    ax2.plot(x, y2, label='Wave 2')
    ax2.set_title('Wave 2')
    ax2.set_ylim(-10, 10)
    ax2.legend()
    
    ax3.clear()
    ax3.plot(x, y_sum, label='Sum of Waves')
    ax3.set_title('Sum of Waves')
    ax3.set_ylim(-10, 10)
    ax3.legend()
    
    plt.draw()

# Создание графиков
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

# Определение слайдеров для амплитуд и частот волн
amplitude1_slider = FloatSlider(min=0, max=10, step=0.1, value=1, description='Amplitude 1')
frequency1_slider = FloatSlider(min=0, max=10, step=0.1, value=1, description='Frequency 1')
amplitude2_slider = FloatSlider(min=0, max=10, step=0.1, value=1, description='Amplitude 2')
frequency2_slider = FloatSlider(min=0, max=10, step=0.1, value=1, description='Frequency 2')

# Создание интерактивных виджетов
interact(update_plot, amplitude1=amplitude1_slider, frequency1=frequency1_slider,
         amplitude2=amplitude2_slider, frequency2=frequency2_slider)

# Отображение графиков и слайдеров
print('окно запущено')
plt.show()
