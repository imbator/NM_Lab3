import matplotlib.pyplot as plt
import numpy as np
from statistics import median
from math import sqrt
# Линейная регрессия методом наименьших квадратов

fig, ax = plt.subplots(figsize=(8, 5))

y = [0.6284, 0.5333, 1.7308, 0.6432, -0.5780, 0.4591, -0.9187, 0.0801, 0.0572,
     0.1068, -0.2154, 1.1865,  -1.8008, 0.4749,  0.9074,  0.6995,  0.4953, -0.1002,
     0.4736,  0.2998,  -0.5902, -0.7734, -0.7450, -1.9645, -0.7455, -0.3919, -0.1660,
     1.0252, -0.6698,  0.4435,  0.7990,  1.1605,  -0.5165,  0.9742,  1.3081, 0.3796,
     0.9562, 3.0667, 2.0931, 2.7852, 2.5597, 1.7934, 1.6830, 2.3352, 0.4085, 1.4136,
     0.2798, -2.2205, -2.9427, -5.2786, -7.7944]
x = np.arange(-1.5, 1.56, 0.06)
print(len(x), len(y))
# требуется найти y = kx + b
# kx(i) + b = y(i_theor)
# найдем C1, C2, C3, C4:
c1, c2, c3, c4, n = sum(x[0:10]), sum(y[0:10]), sum(x[0:10]**2), sum((x[0:10]*y[0:10])), len(x[0:10])
k = (c4*n - c1*c2) / (n*c3 - c1**2)
b = (c2 - c1*k) / n
func = k*x[0:10] + b
t = np.linspace(-1.7, 1.7, 200)
linear = k*t + b
# нанесем точки
for i in range(0, 10):
    ax.plot(x[i], y[i], 'o', color='r', markersize=10)
    # print(f'Нанесена точка: {x[i], y[i]}')
ax.plot(x[0:10], func, label='Regression')
ax.grid(True, which='both')
ax.axis([-1.6, -0.9, -1, 2])
ax.title.set_text('Linear regression for the first 10 points')
plt.xlabel("x")
plt.ylabel("y")
plt.subplots_adjust(right=0.58)
ax.plot(t, linear, '--', color='b', markersize=2)
# Медиана, среднее значение, ср. кв. отклонение, cр. кв. отклонение смещения

plt.text(0.6, 0.8, 'Параметры регрессии', fontsize=17, color='r',  transform=plt.gcf().transFigure)

plt.text(0.6, 0.7, f'Медиана: {median(y)}', fontsize=14, transform=plt.gcf().transFigure)
plt.text(0.6, 0.6, f'Среднее значение: {round(np.average(y), 4)}', fontsize=14, transform=plt.gcf().transFigure)

ort_sigma = round(np.std(y), 4)
sigma = sqrt(10/(10-1))*ort_sigma

plt.text(0.6, 0.5, f'Ср кв. откл: {round(sigma, 4)}', fontsize=14, transform=plt.gcf().transFigure)
plt.text(0.6, 0.4, f'Ср кв. откл. смещения: {ort_sigma}', fontsize=14, transform=plt.gcf().transFigure)

# коэффициент корреляции

corr = np.corrcoef([x[0:10], y[0:10]])[0, 1]


plt.text(0.6, 0.3, f'Коэфф. корреляции: {round(corr, 4)}', fontsize=14, transform=plt.gcf().transFigure)
ax.legend()
plt.show()
