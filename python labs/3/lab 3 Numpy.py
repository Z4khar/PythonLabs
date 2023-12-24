import numpy as np
# 1 Cоздание массива
print("#1 Создание массива")
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
#1.1 Cоздание нулевого и еденичного массива заданного размера
print("#1.1 Нулевой и единичный массив")
A1 = np.zeros((2, 3), 'int')
B1 = np.ones((3, 2))
print(A1)
print(B1)
#1.2 массив чисел от From (включая) до To (не включая) с шагом Step
print("#1.2 Массив с шагом")
From = 2.5
To = 7
Step = 0.5
A2 = np.arange(From, To, Step)
print(A2)
# 2 Доступ к элементам, cрезы
print("#2 Доступ к элементам, срезы")
print(A[0][2], A[1,0], A[1])
print("#2.1")
A = np.arange(5)
print(A)
print(A[-1])
print(A[1:4])
#2.2 Доступ к элементам массива через булев индексный массив
print("#2.2 доступ к элементам через булев индексный массив")
A3 = np.array([[1, 2, 3], [4, 5, 6]])
I = np.array([[False, False, True], [ True, False, True]])
print(A3[I])
A3[I]=0
print(A3)
# 3 Форма массива и ее изменение
print("#3 форма массива и ее изменение")
A = np.arange(24)
B = A.reshape(4, 6)
C = A.reshape(4, 3, 2)
print(A) # исходный массив
print('B\n', B)
print('\nC\n', C)
# 3.1 размерность массива
print("#3.1 размерность массива")
print(C.ndim, len(C.shape), C.shape, A.size)
# 3.2 соединение в одномерный массив
print("#3.2 соединение в одномерном массиве")
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.ravel())
# 3.3 изменение размерности (по осям и сторлбцам)
print("#3.3 изменение размерности")
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.reshape(3, 2))
# 4 Перестановка осей и траспонирование
print("#4 перестановка и транспонирование")
pA = np.array([[1, 2, 3], [4, 5, 6]])
print('\nA\n',A)
print('\nA data\n', A.ravel())
B = A.T
print('\nB\n', B)
print('\nB data\n', B.ravel())
#5 Объединение массивов
print("#5 объединение массива")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("\nA\n", A)
B = A[::-1]
print("\nB\n", B)
C = A[:, ::-1]
print("\nC\n",C)
D = np.stack((A, B, C))
print("Объединенный массив: ")
print(D.shape)
print(D)
#6 Копирование данны 
print("#6 копирование данных")
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.repeat(A, 2))
# 6.1 сбор повторяющихся данных в одну ось
print("#6.1 сбор повторяющихся данных в одну ось")
B = np.repeat(A, 2).reshape(A.shape[0], A.shape[1], -1)
print(B)
#7 Математические операции над элементами массива 
print("#7 математические операции над элементами массива")
print("7.1")
A = np.array([[-1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
B = np.array([[1., -2., -3.], [7., 8., 9.], [4., 5., 6.], ])
C = A + B
D = A - B
E = A * B
F = A / B
G = A ** B
print('+\n', C, '\n')
print('-\n', D, '\n')
print('*\n', E, '\n')
print('/\n', F, '\n')
print('**\n', G, '\n')
print("7.2")
A = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
B = np.exp(A)
C = np.log(B)
print('A', A, '\n')
print('B', B, '\n')
print('C', C, '\n')
#8 Матричное умножение
print("8 матричное умножение")
# скаляры
A = 2
B = 3
print(np.dot(A, B), '\n')

# вектор и скаляр
A = np.array([2., 3., 4.])
B = 3
print(np.dot(A, B), '\n')

# вектора
A = np.array([2., 3., 4.])
B = np.array([-2., 1., -1.])
print(np.dot(A, B), '\n')

# тензор и скаляр
A = np.array([[2., 3., 4.], [5., 6., 7.]])
B = 2
print(np.dot(A, B), '\n')
 
