from math import sin, cos, sqrt

N = 12  

def f1(x):
    return sin(x[2] - N / 5) - 0.5 * x[1] * cos(x[1] + 7 * x[0]) / (N ** 2)
def f2(x):
    return ((x[0] - 3 * x[1]) * (x[2] + N / 4) - sqrt(abs(x[0])) * x[1]) / (N ** 2)
def f3(x):
    return x[0] * x[1] / (N ** 3) - sin(x[2] * x[1] + 0.5)
def f4(x):
    return cos(x[3] * x[0] - 1.5) + x[0] / (N ** 2)

# Векторная функция F(x), возвращает список значений f1, f2, f3, f4 для заданного x
def F(x):
    return [f1(x), f2(x), f3(x), f4(x)]

# Сложение двух векторов одинаковой длины
def vector_add(a, b):
    return [a[i] + b[i] for i in range(len(a))]  

# Умножение вектора на скаляр
def vector_scalar_mult(vec, scalar):
    return [v * scalar for v in vec]  

# Вычитание одного вектора из другого
def vector_sub(a, b):
    return [a[i] - b[i] for i in range(len(a))]  

# Нахождение Евклидовой нормы 
def kMod(x):
    return sqrt(sum(xi ** 2 for xi in x))  

def main():
    i, max_i = 0, 1000000  
    eps = 0.001  
    x = [1.8, 0.65, -5.6, 1.7]  # Начальное приближение вектора X (Можно выстовить любое)
    lambda_coeff = 0.1  

    while True:
        i += 1  
        F_val = F(x)  
        x_new = vector_add(x, vector_scalar_mult(F_val, lambda_coeff))  

        if kMod(vector_sub(x_new, x)) <= eps or i >= max_i:
            break
        x = x_new  

    if i == max_i:
        print("Достигнуто максимальное число итераций")
    else:
        print(f"Количество итераций: {i}") 
        print("Решение:", x)
        print("Норма невязки:", kMod(F(x))) 

if __name__ == "__main__":
    main()