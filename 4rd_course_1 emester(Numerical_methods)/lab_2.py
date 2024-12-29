import numpy as np
import matplotlib.pyplot as plt
import copy

x_start, x_end = 1, 2  
y_initial = 1
h = 0.1

# Функция задача Коши
def f(x, y):
    return (y ** 2 + y * x) / x ** 2

# Функция точного решения
def exact_solution(x):
    return -x / (np.log(x) - 1)

# Метод Эйлера
def euler_method(x0, y0, h, steps):
    x_values = [x0]
    y_values = [y0]

    for i in range(steps):
        y0 += h * f(x0, y0)  
        x0 += h  
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# Усовершенствованный метод Эйлера-Коши с итерациями
def improved_euler_cauchy(x0, y0, h, steps, max_iterations=4):
    x_values = [x0]
    y_values = [y0]

    for i in range(steps):  
        y_predict = y0 + h * f(x0, y0)
        y_next = y_predict  

        for k in range(max_iterations):  
            y_next = y0 + (h / 2) * (f(x0 + h, y_next) + f(x0, y0))

        x0 += h  
        y0 = y_next  
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# Вычисление точного решения
def calculate_exact(x0, xf, h):
    xs = np.arange(x0, xf + h, h)  
    ys = [exact_solution(x) for x in xs] 
    return xs, ys

# Функция для вычисления Рунге h = 0.2
def runge_correction(y_values_h, y_values_2h, p):
    n = len(y_values_h) - 1  
    n2 = len(y_values_2h) - 1  
    R = [0] * (n + 1)

    for k in range(1, n2 + 1):  
        R[2 * k] = (y_values_h[2 * k] - y_values_2h[k]) / (2 ** p - 1)
        y_values_h[2 * k] += R[2 * k]  

    for k in range(n2):  
        R[2 * k + 1] = (R[2 * k] + R[2 * k + 2]) / 2  
        y_values_h[2 * k + 1] += R[2 * k + 1] 

    return y_values_h  

x_exact, y_exact = calculate_exact(x_start, x_end, h)  

n = int((x_end - x_start) / h) 
x_values_euler, y_values_euler = euler_method(x_start, y_initial, h, n)
x_values_cauchy, y_values_cauchy = improved_euler_cauchy(x_start, y_initial, h, n)

h2 = 2 * h  
n2 = n // 2  
_, y_values_2h = improved_euler_cauchy(x_start, y_initial, h2, n2)  

p = 2  
y_values_runge = runge_correction(copy.deepcopy(y_values_cauchy), y_values_2h, p)

methods = ["Явный метод Эйлера", "Усовершенствованный метод Эйлера", "Метод Рунге"]
results = [y_values_euler, y_values_cauchy, y_values_runge]

for method, y_values in zip(methods, results):
    print(f"\n{method}\n")
    print(f"    x    |     y    |  answer  |   eps   ")
    total_error = 0
    for i, (x, y, exact) in enumerate(zip(x_exact, y_values, y_exact)):
        error = y - exact
        total_error += abs(error)
        print(f"{x:.6f} | {y:.6f} | {exact:.6f} | {error:.6f}")
    print(f"\nОбщая погрешность: {total_error}\n")

plt.figure(figsize=(10, 6))
plt.plot(x_exact, y_exact, label="Точное решение", color="black", linewidth=2)
plt.plot(x_values_euler, y_values_euler, label="Явный метод Эйлера", color="red", linestyle='--')
plt.plot(x_values_cauchy, y_values_cauchy, label="Усовершенствованный метод Эйлера", linestyle='-.')
plt.plot(x_values_cauchy, y_values_runge, label="Метод Рунге", linestyle=':')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()