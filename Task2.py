'''
2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​

import numpy as np

random_array = np.random.rand(5) # массив из 5 случайных чисел

print(random_array)
'''


import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
data_x = np.random.rand(5)  # Первый набор из 5 случайных чисел
data_y = np.random.rand(5)  # Второй набор из 5 случайных чисел
print(f'data_x: {data_x}')
print(f'data_y: {data_y}')

# Построение диаграммы рассеяния

plt.figure(figsize=(10, 6)) # Установка размера графика

plt.scatter(data_x, data_y, color='blue', alpha=0.7, edgecolor='black') # Создание диаграммы рассеяния

plt.title('Диаграмма рассеяния двух наборов случайных данных')  # Заголовок
plt.xlabel('Набор данных X')  # Подпись оси X
plt.ylabel('Набор данных Y')  # Подпись оси Y
plt.grid(True)  # Включение сетки
plt.show()  # Отображение диаграммы рассеяния