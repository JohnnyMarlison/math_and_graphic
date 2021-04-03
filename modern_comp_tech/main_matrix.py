from matrix import *


n = int(input("Введите размерность матрицы n = "))
MyMatr = MakeMatr(n, -5, 5)
PrintMatr(MyMatr)

# поиск максимального и минимального элемента
mx = MyMatr.max()
mn = MyMatr.min()
print('\nMax: ', "{0: 1.0f}".format(mx), '\nMin: ', "{0: 1.0f}".format(mn))

# поиск местоположения максимального и минимального
i1, j1 = np.where(MyMatr == mx)
i2, j2 = np.where(MyMatr == mn)
print('IDMax', i1, j1)
print('IDMin', i2, j2, '\n')

swape_cols(MyMatr, j1, j2)
PrintMatr(MyMatr)

# сумма элементов главной диагонали
s = 0
for i in range(len(MyMatr)):
    for j in range(len(MyMatr)):
        if i == j:
            s += MyMatr[i][j]

print('\n Сумма главной диагонали: ', "{0: 2.0f}".format(s))