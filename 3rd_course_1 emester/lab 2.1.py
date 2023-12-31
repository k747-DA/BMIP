import copy
import numpy as np
from math import *

print('------------------Вариант 15------------------')
print('----------------------№ 1---------------------')
print('----------------Метод: Точные-----------------')
print('----------Задача: Квадратного корня-----------')

# функция просто печатает матрицу A, выводя каждую строку отдельно.
def print_matrix(A):  # вывод матрицы А
    for strA in A:
        print(strA)


#  функция создает минор матрицы A для заданных индексов i и j.
#  Она удаляет i-тую строку и j-тый столбец из матрицы A и возвращает результирующую матрицу M.
def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):  # функция для нахождение определителя
    m = len(A)  # вычисляется длина и ширина матрицы введеной
    n = len(A[0])
    if m != n:  # если m и n не совпадают определитель не найдется и возрощает None
        return None
    if n == 1:  # если равен 1x1, то у нас 1 элемент в матрице  определитель будет равен этому элементу
        return A[0][0]
    signum = 1  # флаг
    determinant = 0  # изначальное значение определителя

    for j in range(n):  # нахождение определителя по формуле
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant

# функция вычисляет обратную матрицу A. Для каждого элемента матрицы A
# она вычисляет соответствующий минор, использует определитель этого минора и определитель матрицы A
# для вычисления элементов обратной матрицы.
def inverse(A):  # нахождение обратной матрецы A
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            tmp = minor(A, i, j)  # берется минор
            if i + j % 2 == 1:  # если сумма строки и остаток от деления столбца на 2 нечетный то появляется минус, если четная то плюс
                result[i][j] = -1 * det(tmp) / det(A)
            else:
                result[i][j] = 1 * det(tmp) / det(A)
    return result

# функция выполняет транспонирование матрицы array,
# возвращая результат в виде новой транспонированной матрицы.
def transpose(array):  # транспонированная матрица
    res = []
    n = len(array)
    m = len(array[0])
    for j in range(m):  # идем по столбцам
        tmp = []  # пустой массив
        for i in range(n):  # идем по строкам
            tmp = tmp + [array[i][j]]  # по элементно строка становится столбцом
        res = res + [tmp]
    return res


matrix = [[151, 4, 2, 2],
          [4, 8, 0, 2],
          [2, 0, 9, -4],
          [2, 2, -4, 12]]
A = transpose(matrix)
print('---------------ОБРАТНАЯ МАТРИЦА---------------')

C = inverse(A)
print_matrix(C)
print('-----------------ОПРЕДЕЛИТЕЛЬ-----------------')

print(det(matrix))


def check_answer():
    print("-------------------ПРОВЕРКА-------------------")

    A = [[151, 4, 2, 2],
         [4, 8, 0, 2],
         [2, 0, 9, -4],
         [2, 2, -4, 12]]

    B = [2 * 15 * np.sin(15), 5 * (np.sin(15) - np.cos(15)), 7 * (np.cos(15) + np.sin(15)), 3 * np.sin(15)]
    for i in range(4):
        print('A*X', i + 1, A[i][0] * X[0] + A[i][1] * X[1] + A[i][2] * X[2] + A[i][3] * X[3])
    print(B)


# Расширенная матрица A|B
A_extend = [[151, 4, 2, 2, 2 * 15 * np.sin(15)],
            [4, 8, 0, 2, 5 * (np.sin(15) - np.cos(15))],
            [2, 0, 9, -4, 7 * (np.cos(15) + np.sin(15))],
            [2, 2, -4, 12, 3 * np.sin(15)]]

T = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

# Заполняем 1 строку матрицы T
for i in range(0, 4):
    if i == 0:
        T[0][i] = np.sqrt(A_extend[0][0])
    else:
        T[0][i] = A_extend[0][i] / T[0][0]

# Заполняем 2 строку матрицы T
for i in range(1, 4):
    if i == 1:
        T[1][i] = np.sqrt(A_extend[1][1] - (T[0][1] ** 2))
    else:
        T[1][i] = (A_extend[1][i] - (T[0][1]) * T[0][i]) / T[1][1]

# Заполняем 3 строку матрицы T
for i in range(2, 4):
    if i == 2:
        T[2][i] = np.sqrt(A_extend[2][2] - (T[0][2] ** 2 + T[1][2] ** 2))
    else:
        T[2][i] = (A_extend[2][i] - (T[0][2] * T[0][i] + T[1][2] * T[1][i])) / T[2][2]

# Заполняем 4 строку матрицы T (единственное значение)
T[3][3] = np.sqrt(A_extend[3][3] - (T[0][3] ** 2 + T[1][3] ** 2 + T[2][3] ** 2))

# Находим bi в матрице T
T[0][4] = A_extend[0][4] / T[0][0]
T[1][4] = (A_extend[1][4] - T[0][1] * T[0][4]) / T[1][1]
T[2][4] = (A_extend[2][4] - (T[0][2] * T[0][4] + T[1][2] * T[1][4])) / T[2][2]
T[3][4] = (A_extend[3][4] - (T[0][3] * T[0][4] + T[1][3] * T[1][4] + T[2][3] * T[2][4])) / T[3][3]

# Находим решение
X = [0, 0, 0, 0]
X[3] = T[3][4] / T[3][3]  # x[4]
X[2] = (T[2][4] - T[2][3] * X[3]) / T[2][2]  # x[3]
X[1] = (T[1][4] - (T[1][2] * X[2] + T[1][3] * X[3])) / T[1][1]  # x[2]
X[0] = (T[0][4] - (T[0][1] * X[1] + T[0][2] * X[2] + T[0][3] * X[3])) / T[0][0]  # x[1]

print('-------------------Матрица T------------------')
for i in range(4):
    for j in range(5):
        print(T[i][j].__round__(3), end='\t')
    print()

print('---Матрица решений. метод квадратного корня:--')
for i in range(4):
    print("X", i + 1, " = ", X[i])

# Проверка
check_answer()