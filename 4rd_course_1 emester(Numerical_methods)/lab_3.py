import numpy as np
import matplotlib.pyplot as plt


x_start, x_end = 0, 1
y_initial = 1
y_prime_initial = 1
h = 0.1

# Приведение ОДУ 2-го порядка к системе 1-го порядка
def f1(x, y, z):
    return z  

def f2(x, y, z):
    return (2 * x * z - 2 * y) / ((x**2) + 1)  

# Функция точного решения
def exact_solution(x):
    return x - x**2 + 1

# Метод Эйлера для системы ОДУ
def euler_method_system(x0, y0, z0, h, steps):
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]

    for i in range(steps):
        y_next = y0 + h * f1(x0, y0, z0)  
        z_next = z0 + h * f2(x0, y0, z0)  
        x0 += h  
        y0, z0 = y_next, z_next

        x_values.append(x0)
        y_values.append(y0)
        z_values.append(z0)

    return x_values, y_values

# Усовершенствованный метод Эйлера-Коши для системы ОДУ
def improved_euler_cauchy_system(x0, y0, z0, h, steps):
    x_values = [x0]
    y_values = [y0]
    z_values = [z0]

    for i in range(steps):
        y_predict = y0 + h * f1(x0, y0, z0)
        z_predict = z0 + h * f2(x0, y0, z0)

        y_next = y0 + (h / 2) * (f1(x0, y0, z0) + f1(x0 + h, y_predict, z_predict))
        z_next = z0 + (h / 2) * (f2(x0, y0, z0) + f2(x0 + h, y_predict, z_predict))

        x0 += h  
        y0, z0 = y_next, z_next

        x_values.append(x0)
        y_values.append(y0)
        z_values.append(z0)

    return x_values, y_values

# Функция для вычисления поправок Рунге
def runge_correction(y_values_h, y_values_2h, p):
    n = len(y_values_h) - 1  
    n2 = len(y_values_2h) - 1  
    R = [0] * (n + 1)  

    for k in range(1, n2 + 1):
        R[2 * k + 1] = (y_values_h[2 * k] - y_values_2h[k]) / (2 ** p - 1) 
        y_values_h[2 * k] += R[2 * k]

    for k in range(n2):
        R[2 * k + 1] = (R[2 * k] + R[2 * k + 2]) / 2  
        y_values_h[2 * k + 1] += R[2 * k + 1]

    return y_values_h

def calculate_exact(x0, xf, h):
    xs = np.arange(x0, xf + h, h)  
    ys = [exact_solution(x) for x in xs] 
    return xs, ys  

x_exact, y_exact = calculate_exact(x_start, x_end, h) 

# Метод Эйлера
n = int((x_end - x_start) / h)  
x_values_euler, y_values_euler = euler_method_system(x_start, y_initial, y_prime_initial, h, n)


# Усовершенствованный метод Эйлера-Коши
x_values_cauchy, y_values_cauchy = improved_euler_cauchy_system(x_start, y_initial, y_prime_initial, h, n)

# Метод Рунге для h = 0.2
h_runge = 2 * 12  
n_runge = int((x_end - x_start) / h_runge)  
x_values_h, y_values_h = improved_euler_cauchy_system(x_start, y_initial, y_prime_initial, h_runge, n_runge)
x_values_2h, y_values_2h = improved_euler_cauchy_system(x_start, y_initial, y_prime_initial, 2 * h_runge, n_runge // 2)

p = 2  
corrected_y_values = runge_correction(y_values_h, y_values_2h, p)  

methods = ["Явный метод Эйлера", "Усовершенствованный метод Эйлера", "Метод Рунге (h=0.2)"]
results = [y_values_euler, y_values_cauchy, corrected_y_values]

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
plt.plot(x_values_cauchy, y_values_cauchy, label="Усовершенствованный метод Эйлера", color="blue", linestyle='-.')
plt.plot(x_values_h, corrected_y_values, label="Метод Рунге (h=0.2)", color="green", linestyle=':')
plt.xlabel("x")
plt.ylabel("y")
plt.title("ОДУ 2 порятдка")
plt.legend()
plt.grid(True)
plt.show()