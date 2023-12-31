import numpy as np
import matplotlib.pyplot as plt
import math

# Создаются списки X и Y, содержащие координаты точек
X = [15.0,     15.1,     15.2,     15.3,     15.4,     15.5,    15.6,     15.7,     15.8,     15.9]
Y = [-0.00091, 0.624825, 1.203832, 1.677044, 1.994648, 2.12132, 2.040105, 1.754519, 1.288629, 0.685062]
# Задается значение переменной n
n = 10

# Выполняется сдвиг массива Y, если Y[i] < 0:
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

# Запрашивается выбор типа аппроксимации:
print ('Сдвинутый массив:\n', Y)
print("Выберите тип аппроксимации:\n1)Логарифмическая\n2)Линейная")

# Логарифмическая аппроксимация
change = int(input())
if change == 1:
    # Ищем решение системы
    sum_ylnx = 0
    sum_lnx = 0
    sum_y = 0
    sum_ln2x = 0
    sum_powx = 0

    # инициализируется нулём и затем увеличивается путем сложения каждого элемента Y[i] умноженного на np.log(X[i]).
    for i in range(0, n):
        sum_ylnx += Y[i] * np.log(X[i])

    # инициализируется нулём и затем увеличивается путем сложения значений np.log(X[i]).
    for i in range(0, n):
        sum_lnx += np.log(X[i])

    # инициализируется нулём и затем увеличивается путем сложения каждого элемента Y[i].
    for i in range(0, n):
        sum_y += Y[i]

    #  инициализируется нулём и затем увеличивается путем сложения квадратов значений np.log(X[i]).
    for i in range (0, n):
        sum_ln2x += pow(np.log(X[i]), 2)

    # инициализируется нулём и затем увеличивается путем сложения квадратов значений X[i] * X[i].
    for i in range(0, n):
        sum_powx += X[i] * X[i]

    # Затем, выводим суммы различных величин
    print(sum_ylnx)
    print(sum_lnx)
    print(sum_y)
    print(sum_ln2x)

    # Вычисляются коэффициенты линейной аппроксимации
    b = (n * sum_ylnx - sum_lnx * sum_y) / (n * sum_ln2x - pow(sum_lnx, 2))
    a = ((1 / n) * sum_y) - ((b / n) * sum_lnx)

    # Выводим проценты коофицента
    print("Коеф-ты:\na = ", a, "\nb = ", b)

    # Зедесь вычисляем коэффициента сглаживания C
    sum_Ex = 0
    # sum_Ex инициализируется нулём и затем увеличивается путем сложения разности (Y[i] - b * np.log(X[i]) - a) умноженной на X[i] для каждого элемента i.
    for i in range(0, n):
        sum_Ex += (Y[i] - b * np.log(X[i])-a)*X[i]
    C = (-sum_Ex) / (sum_powx)
    print("Сглаживание C = ", C)

    # Здесь вычисляется среднеквадратичное отклонение G
    G = 0
    sum_G = 0
    # sum_G инициализируется нулём и затем увеличивается путем сложения квадратов разности (Y[i] - b * np.log(X[i]) - a) для каждого элемента i.
    # G вычисляется как квадратный корень из отношения sum_G к количеству элементов n.
    for i in range(0, n):
        sum_G += pow((Y[i] - b * np.log(X[i]) - a), 2)
    G = math.sqrt(sum_G / n)
    print("Среднеквадратичное отклонение равно: ", G)

    # Вычисляем погрешность flt
    flt = 0
    # flt инициализируется нулём и затем увеличивается путем сложения квадратов разности (Y[i] - (b * np.log(X[i]) + a)) для каждого элемента i.
    for i in range(0, n):
        flt += pow(Y[i] - (b * np.log(X[i]) + a), 2)
    print("Погрешность: ", flt)

    # Здесь вычисляем аппроксимированные значения y_ap
    # В цикле for для каждого элемента i от 0 до n, вычисляется значение b * np.log(X[i]) + a + C * X[i], которое добавляется в список y_ap
    y_ap = []
    for i in range(0, n):
        y_ap.append(b*np.log(X[i])+a+C*X[i])
    print(y_ap)

    # Здесь вычисляются начальные значения y_start до применения сглаживания
    # В цикле for для каждого элемента i от 0 до n, вычисляется значение b * np.log(X[i]) + a, которое добавляется в список y_start.
    y_start=[]
    for i in range(0, n):
        y_start.append(b*np.log(X[i])+a)

    # Визуализация
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
    # Ищем решение системы
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

    # Поиск коеффициентов
    a = (sum_x * sum_y - n * sum_xy) / (pow(sum_x, 2) - n * sum_powx)
    b = (sum_x * sum_xy - sum_powx * sum_y) / (pow(sum_x, 2) - n * sum_powx)
    print("Коеф-ты:\na = ", a, "\nb = ", b)

    # Отклонение
    # sum_Ex инициализируется нулём и затем увеличивается путем сложения выражения ((a * X[i] + b) - Y[i]) * X[i] для каждого элемента i.
    sum_Ex = 0
    for i in range(0, n):
        sum_Ex += ((a * X[i] + b) - Y[i]) * X[i]
    print("Ex", sum_Ex)
    C = (-sum_Ex) / (sum_powx)
    print("Сглаживание C = ", C)

    # Среднеквадратичное отклонение
    # sum_G инициализируется нулём и затем увеличивается путем сложения квадратов выражения (Y[i] - (a * X[i] + b)) для каждого элемента i
    G = 0
    sum_G = 0
    for i in range(0, n):
        sum_G += pow((Y[i] - (a * X[i] + b)), 2)
    G = math.sqrt(sum_G/n)
    print("Среднеквадратичное отклонение равно: ", G)

    # Погрешность
    # flt инициализируется нулём и затем увеличивается путем сложения квадратов выражения (Y[i] - (a * X[i] + b)) для каждого элемента i
    flt = 0
    for i in range(0, n):
        flt += pow(Y[i] - (a * X[i] + b), 2)
    print("Погрешность: ", flt)
    print("y = a * x - b до сглаживания")

    #после сглаживания
    # В цикле for для каждого элемента i от 0 до n, вычисляется значение (a * X[i] + b) + C * X[i], которое добавляется в список y_ap
    y_ap = []
    for i in range(0, n):
        y_ap.append((a * X[i] + b) + C * X[i])
    print(y_ap)
    y_start = []

    # до сглаживания
    # В цикле for для каждого элемента i от 0 до n, вычисляется значение a * X[i] + b, которое добавляется в список y_start
    for i in range(0, n):
        y_start.append(a * X[i] + b)

    # Визуализация
    plt.plot(X, Y, 'ro', label='Узлы')
    plt.plot(X, y_ap, 'b', label='После сглаживания')
    plt.plot(X, y_start, 'y', label='y=a*x-b до сглаживания')
    plt.title('Аппроксимация(Линейная)')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()