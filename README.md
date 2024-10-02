# AZ03_Data_Visualization

## Задание 1. 
Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.

.# Параметры нормального распределения

mean = 0 # Среднее значение

std_dev = 1 # Стандартное отклонение

num_samples = 1000 # Количество образцов

.# Генерация случайных чисел, распределенных по нормальному распределению

data = np.random.normal(mean, std_dev, num_samples)

## Задание 2. 
Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​

import numpy as np

random_array = np.random.rand(5) # массив из 5 случайных чисел

print(random_array)
