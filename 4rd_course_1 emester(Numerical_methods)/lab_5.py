import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Параметры задачи
variant_number = 12  
alpha_param = 0.5 + 0.1 * variant_number  # Альфа
L = 1.0  # Длина области по пространственной координате x
T = 1.0  # Время моделирования
Nx = 10  # Количество точек разбиения по x (пространственная сетка)
Nt = 10  # Количество временных слоёв 
dx = L / Nx  # Шаг по пространству (расстояние между узлами)
dt = T / Nt  # Шаг по времени (промежуток между слоями)
gamma_s_p = (dt / dx) ** 2  # Параметр устойчивости схемы (отношение шагов по времени и пространству)


def rhs_function(x, t):
    return 2 * (alpha_param**2 - 1) / (x + alpha_param * t + 1)**2

# Начальные условия
def initial_condition(x):
    return 1 / (1 + x)  

def initial_velocity(x):
    return -alpha_param / (1 + x)**3  

def left_boundary(t):
    return 1 / (alpha_param * t + 1)  

def right_boundary(t):
    return 1 / (alpha_param * t + 2)  

grid_x = np.linspace(0, L, Nx + 1)  
grid_t = np.linspace(0, T, Nt + 1)  

solution_grid = np.zeros((Nt + 1, Nx + 1)) 

solution_grid[0, :] = initial_condition(grid_x)  

solution_grid[1, 1:-1] = ( 
    solution_grid[0, 1:-1]  
    + dt * initial_velocity(grid_x[1:-1])  
    + 0.5 * gamma_s_p * (solution_grid[0, 2:] - 2 * solution_grid[0, 1:-1] + solution_grid[0, :-2]) 
    + dt**2 * rhs_function(grid_x[1:-1], grid_t[0]) / 2  
)

solution_grid[:, 0] = left_boundary(grid_t)  
solution_grid[:, -1] = right_boundary(grid_t)  

for n_stop in range(1, Nt): 
    for spatial_step in range(1, Nx): 
        solution_grid[n_stop + 1, spatial_step] = (  
            2 * (1 - gamma_s_p) * solution_grid[n_stop, spatial_step]  
            + gamma_s_p * (solution_grid[n_stop, spatial_step - 1] + solution_grid[n_stop, spatial_step + 1]) 
            - solution_grid[n_stop - 1, spatial_step] 
            + dt**2 * rhs_function(grid_x[spatial_step], grid_t[n_stop])  
        )
    solution_grid[n_stop + 1, 0] = left_boundary(grid_t[n_stop + 1])  
    solution_grid[n_stop + 1, -1] = right_boundary(grid_t[n_stop + 1])  

approximation_error = gamma_s_p * dx**2

print("=== Параметры задачи ===")
print(f"Длина отрезка (L): {L}\n"
      f"Шаг по x (dx): {dx:.4f}\n"
      f"Шаг по времени (dt): {dt:.4f}\n"
      f"Параметр γ: {gamma_s_p:.4f} (устойчивость: {'да' if gamma_s_p <= 1 else 'нет'})")

print("\n=== Резултаты ===")
table_headers = ["x \\ t"] + [f"{t:.2f}" for t in grid_t]
table_rows = []

for i, x in enumerate(grid_x):
    row = [f"{x:.2f}"] + [f"{solution_grid[j, i]:.4f}" for j in range(Nt + 1)]
    table_rows.append(row)

print(tabulate(table_rows, headers=table_headers, tablefmt="grid"))

print(f"=== Исследование погрешности ==="
      f"Погрешность аппроксимации: {approximation_error:.5e}")

plt.figure(figsize=(10, 6))
time_to_plot = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for time_idx, current_time in enumerate(grid_t):
    if current_time in time_to_plot:
        plt.plot(grid_x, solution_grid[time_idx, :], '-o', label=f" Временном слой t = {current_time:.2f}")

plt.xlabel("Координата x")
plt.ylabel("u(x, t)")
plt.title("Численное решение гиперболического уравнения")
plt.legend(loc='upper right')
plt.grid()
plt.show()