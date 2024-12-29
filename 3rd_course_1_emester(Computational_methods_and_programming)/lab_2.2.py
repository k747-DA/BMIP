import copy
import numpy as np

print('------------------№ 2-------------------')
print('----------Метод: Итерационные-----------')
print('-------Задача: Минемальных невязок------')


epsil = 0.000001

A = [
    [151, 4, 2, 2],
    [4, 8, 0, 2],
    [2, 0, 9, -4],
    [2, 2, -4, 12]
]

B = np.matrix([
    [2 * 15 * np.sin(15)],
    [5 * (np.sin(15) - np.cos(15))],
    [7 * (np.cos(15) + np.sin(15))],
    [3 * np.sin(15)]
])

X = np.matrix([
    [0],
    [0],
    [0],
    [0]
])

# функция minor создает и возвращает минор матрицы A
def minor(A, i, j):
    M = copy.deepcopy(A) 
    del M[i]  
    for i in range(len(A[0]) - 1):
        del M[i][j]  
    return M


# Функция det вычисляет определитель матрицы A рекурсивно, используя миноры.
def det(A):  
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1  
    determinant = 0 

    for j in range(n): 
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant

# Функция trans выполняет транспонирование матрицы array,
def trans(array):  
    res = []
    n = len(array) 
    m = len(array[0])
    for j in range(m):  
        tmp = [] 
        for i in range(n):  
            tmp = tmp + [array[i][j]]  
        res = res + [tmp]  
    return res

# Функция inverse вычисляет обратную матрицу A с использованием миноров и определителя.
def inverse(A):  
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(A)):  
        for j in range(len(A[0])): 
            tmp = minor(A, i, j)  
            if i + j % 2 == 1:  
                result[i][j] = -1 * det(tmp) / det(A)
            else:
                result[i][j] = 1 * det(tmp) / det(A)
    return result


def print_matrix(A): 
    for strA in A:
        print(strA)

#  цикл использует метод итераций
#  для нахождения вектора решения системы уравнений с заданной точностью epsil.
counter = 0
while np.linalg.norm(A * X - B) > epsil:
    r = A * X - B  
    t = np.dot((A * r).transpose(), r) / (np.linalg.norm(A * r) ** 2)
    X = X - float(t) * r
    counter += 1

print('---------------Матрица A:---------------')
print_matrix(A)
print("---------------Матрица B:---------------")
print_matrix(B)
print('----------------------------------------')
print('Вектор решения с точностью ', epsil, ': \n', X)
print('----------------------------------------')
print('Количество итераций: ', counter)
print("-----Направление невязки (вектора)------")
print(A*X-B) 
print('----------------------------------------')
print('Определитель матрицы: ', det(A))
P = trans(A)
print('------------Обратная матрица------------')
C = inverse(P)
print_matrix(C)