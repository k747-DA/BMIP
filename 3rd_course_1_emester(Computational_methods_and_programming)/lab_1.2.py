import numpy as np
import matplotlib.pyplot as plt
import math

# Создаются списки X и Y, содержащие координаты точек
X = [15.0,     15.1,     15.2,     15.3,     15.4,     15.5,    15.6,     15.7,     15.8,     15.9]
Y = [-0.00091, 0.624825, 1.203832, 1.677044, 1.994648, 2.12132, 2.040105, 1.754519, 1.288629, 0.685062]
# Задается значение переменной n
n = 10

min = 100
Y_C = []
for i in range(0, n):
    if Y[i] < 0:
        if Y[i] < min:
            min = Y[i]
min = abs(math.floor(min))
print('Сдвиг по Y на: ', min)


for i in range(0, n):
    Y[i] += min

print ('Сдвинутый массив:\n', Y)
print("Выберите тип аппроксимации:\n1)Логарифмическая\n2)Линейная")

change = int(input())
if change == 1:
    sum_ylnx = 0
    sum_lnx = 0
    sum_y = 0
    sum_ln2x = 0
    sum_powx = 0

    for i in range(0, n):
        sum_ylnx += Y[i] * np.log(X[i])

    for i in range(0, n):
        sum_lnx += np.log(X[i])

    for i in range(0, n):
        sum_y += Y[i]

    for i in range (0, n):
        sum_ln2x += pow(np.log(X[i]), 2)

    for i in range(0, n):
        sum_powx += X[i] * X[i]

    print(sum_ylnx)
    print(sum_lnx)
    print(sum_y)
    print(sum_ln2x)

    b = (n * sum_ylnx - sum_lnx * sum_y) / (n * sum_ln2x - pow(sum_lnx, 2))
    a = ((1 / n) * sum_y) - ((b / n) * sum_lnx)

    print("Коеф-ты:\na = ", a, "\nb = ", b)

    sum_Ex = 0
    for i in range(0, n):
        sum_Ex += (Y[i] - b * np.log(X[i])-a)*X[i]
    C = (-sum_Ex) / (sum_powx)
    print("Сглаживание C = ", C)

    G = 0
    sum_G = 0
    for i in range(0, n):
        sum_G += pow((Y[i] - b * np.log(X[i]) - a), 2)
    G = math.sqrt(sum_G / n)
    print("Среднеквадратичное отклонение равно: ", G)

    flt = 0
    for i in range(0, n):
        flt += pow(Y[i] - (b * np.log(X[i]) + a), 2)
    print("Погрешность: ", flt)

    y_ap = []
    for i in range(0, n):
        y_ap.append(b*np.log(X[i])+a+C*X[i])
    print(y_ap)

    y_start=[]
    for i in range(0, n):
        y_start.append(b*np.log(X[i])+a)

    plt.plot(X, Y, 'ro', label='Узлы')
    plt.plot(X, y_ap, 'b', label='После сглаживания')
    plt.plot(X, y_start, 'y', label='y = a * ln(x) + b до сглаживания')
    plt.title('Аппроксимация(Логарифмическая)')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# Линейная аппроксимация если выбрана 2
else:
    sum_y = 0
    sum_x = 0
    sum_powx = 0
    sum_powy = 0
    sum_xy = 0
    for i in range(0, n):
        sum_y += Y[i]
    for i in range(0, n):
        sum_x += X[i]
    for i in range(0, n):
        sum_powx += X[i] * X[i]
    for i in range(0, n):
        sum_powy += Y[i] * Y[i]
    for i in range(0, n):
        sum_xy += X[i] * Y[i]
    print("Суммы")
    print(sum_y)
    print(sum_x)
    print(sum_powx)
    print(sum_powy)
    print(sum_xy)

    a = (sum_x * sum_y - n * sum_xy) / (pow(sum_x, 2) - n * sum_powx)
    b = (sum_x * sum_xy - sum_powx * sum_y) / (pow(sum_x, 2) - n * sum_powx)
    print("Коеф-ты:\na = ", a, "\nb = ", b)

    sum_Ex = 0
    for i in range(0, n):
        sum_Ex += ((a * X[i] + b) - Y[i]) * X[i]
    print("Ex", sum_Ex)
    C = (-sum_Ex) / (sum_powx)
    print("Сглаживание C = ", C)

    G = 0
    sum_G = 0
    for i in range(0, n):
        sum_G += pow((Y[i] - (a * X[i] + b)), 2)
    G = math.sqrt(sum_G/n)
    print("Среднеквадратичное отклонение равно: ", G)

    flt = 0
    for i in range(0, n):
        flt += pow(Y[i] - (a * X[i] + b), 2)
    print("Погрешность: ", flt)
    print("y = a * x - b до сглаживания")

    y_ap = []
    for i in range(0, n):
        y_ap.append((a * X[i] + b) + C * X[i])
    print(y_ap)
    y_start = []

    for i in range(0, n):
        y_start.append(a * X[i] + b)

    plt.plot(X, Y, 'ro', label='Узлы')
    plt.plot(X, y_ap, 'b', label='После сглаживания')
    plt.plot(X, y_start, 'y', label='y=a*x-b до сглаживания')
    plt.title('Аппроксимация(Линейная)')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()