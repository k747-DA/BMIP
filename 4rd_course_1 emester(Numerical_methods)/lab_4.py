# Реализация метода Рунге Кутты 3 порядка а)
# Реализация метода предиктора-корректора Адамса
import math
import matplotlib.pyplot as plt

def f(x):
    return math.log(-1 + pow(math.e, pow(math.e,x)))

def df(x, y):
    return pow(math.e, x - y) + pow(math.e, x)

def PrintVectors(x, y, answer, eps):
    print("    x    |     y    |  answer  |   eps   ")
    for i in range(len(x)):
        print(f"{x[i]:.6f} | {y[i]:.6f} | {answer[i]:.6f} | {eps[i]:.6f}")
    print()

def PrintVectors2(x, y, y2, eps):
    print("    x    |   method |   runge  |   eps   ")
    for i in range(len(x)):
        print(f"{x[i]:.6f} | {y[i]:.6f} | {y2[i]:.6f} | {eps[i]:.6f}")
    print()

# Реализация метода Рунге-Кутты 3-го порядка
def runge_kutta(h, xi, yi):
    k1 = df(xi, yi)
    k2 = df(xi + h/2, yi + k1*h/2)
    k3 = df(xi + h, yi - h*k1 + k2*h*2)
    y_next = yi + (k1 + 4*k2 + k3) * h / 6
    return y_next

h1 = 0.1  
a = 0.0   
b = 1.0   
n = int((b-a)/h1) + 1 
x = [a + i*h1 for i in range(n)]  

# Точное решение для сравнения
answer = [f(xi) for xi in x]

# Начальное приближение для метода Рунге-Кутты
y1 = [0 for i in range(n)]
y1[0] = 0.541325  

# Применение метода Рунге-Кутты для первых 4 шагов
for i in range(0, 4):
    y1[i+1] = runge_kutta(h1, x[i], y1[i])

# Применение метода Адамса (предсказание и коррекция)
for i in range(4, n-1):
    # Предсказание по методу Адамса
    predictor = y1[i] + h1 * (23/12 * df(x[i], y1[i]) - 16/12 * df(x[i-1], y1[i-1]) + 5/12 * df(x[i-2], y1[i-2]))
    # Коррекция по методу Адамса
    y1[i+1] = y1[i] + h1 * (5/12 * df(x[i+1], predictor) + 8/12 * df(x[i], y1[i]) - 1/12 * df(x[i-1], y1[i-1]))

# Расчет погрешностей
eps = [0 for i in range(n)]
for i in range (0, n):
    eps[i] = y1[i] - answer[i]

# Нормированная погрешность
norm = 0
for i in range (0, n):
    norm += eps[i]**2
norm = math.sqrt(norm)

# Печать результатов для Рунге-Кутты + Адамса
print("\tРунге Кутта + Адамс\n")
PrintVectors(x, y1, answer, eps)
print("Общая погрешность: ", norm, "\n")

# Уточнение методом Рунге с шагом h2
h2 = 0.2  # Новый шаг
p = 3  # Параметр метода Рунге
r = 2  # Параметр сходимости

# Инициализация массива для уточненных значений
y2 = [0 for i in range(n)]
y2[0] = 0.541325  

# Применение метода Рунге с шагом h2 для первых 6 шагов
R = [0 for i in range(n)]
for i in range(0, 6, 2):
    y2[i+2] = runge_kutta(h2, x[i], y2[i])

# Применение метода Адамса с уточнением для оставшихся шагов
for i in range(6, n-2, 2):
    # Предсказание по методу Адамса
    predictor = y2[i] + h2 * (55/24 * df(x[i], y2[i]) - 59/24 * df(x[i-2], y2[i-2]) + 37/24 * df(x[i-4], y2[i-4]) - 3/8 * df(x[i-6], y2[i-6]))
    # Коррекция по методу Адамса
    y2[i+2] = y2[i] + h2 * (9/24 * df(x[i+2], predictor) + 19/24 * df(x[i], y2[i]) - 5/24 * df(x[i-2], y2[i-2]) + 1/24 * df(x[i-4], y2[i-4]))

# Уточнение значений с использованием Рунге
for i in range(2, n, 2):
    R[i] = (y1[i]-y2[i])/(math.pow(r, p) - 1)
    y2[i] = y1[i] + R[i]

for i in range(1, n, 2):
    R[i] = (R[i+1] + R[i-1])/2
    y2[i] = y1[i] + R[i]

# Пересчет погрешности для уточненного решения
eps = [0 for i in range(n)]
for i in range (0, n):
    eps[i] = y2[i] - answer[i]

# Нормированная погрешность для уточненного решения
norm = 0
for i in range (0, n):
    norm += eps[i]**2
norm = math.sqrt(norm)

print("\tУточнение методом Рунге\n")
PrintVectors(x, y2, answer, eps)
print("Общая погрешность: ", norm, "\n")

plt.plot(x, y1, label='Рунге-Кутты + Адамс', linestyle='-', linewidth=3)
plt.plot(x, y2, label='Уточнение методом Рунге', linestyle='--', linewidth=4)
plt.plot(x, answer, label='Точное решение', linestyle=':', linewidth=6)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Сравнение методов')
plt.grid(True)  
plt.show()
