import numpy as np
import matplotlib.pyplot as plt

# Создаем массив Data, содержащий пары значений [x, y], x и y представляют собой координаты точек на плоскости.
Data = [[15.0, -0.00091],
        [15.1, 0.624825],
        [15.2, 1.203832],
        [15.3, 1.677044],
        [15.4, 1.994648],
        [15.5, 2.12132],
        [15.6, 2.040105],
        [15.7, 1.754519],
        [15.8, 1.288629],
        [15.9, 0.685062],
        [16.0, 0.00091]] 

for j in range(0, 9, 2): 
    print(j)
    Matrix = np.array([[Data[j][0] ** 2, Data[j][0], 1],
                       [Data[j + 1][0] ** 2, Data[j + 1][0], 1],
                       [Data[j + 2][0] ** 2, Data[j + 2][0], 1]])
    print(Matrix)

    Y = np.array([Data[j][1], Data[j+1][1], Data[j + 2][1]])

    coeff = np.linalg.solve(Matrix, Y)
    print(coeff)
    a = coeff[0]
    b = coeff[1]
    c = coeff[2]

    if j == 8:
        x = np.linspace(Data[j][0], Data[j + 1][0], 10) 
    else:
        x = np.linspace(Data[j][0], Data[j + 2][0], 10)

    y = a * x ** 2 + b * x + c

    plt.plot(x, y, '-')


plt.scatter([point[0] for point in Data], [point[1] for point in Data], c='k')
plt.title("Квадратичный сплайн дефекта 2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

