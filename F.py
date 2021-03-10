from matplotlib.pyplot import *
from numpy import *

#Проверяем является ли фигура замкнутой - первая и последняя коордианты совпадают:
def closed_fig(P):
    return (P[0][0] == P[len(P) - 1][0]) and (P[0][1] == P[len(P) - 1][1])

#Ищем "центр" фигуры (среднее арифметическое вершин):
def find_center(P):
    n = len(P)
    if closed_fig(P):
        n -= 1
    sum_x = 0
    sum_y = 0
    for i in range(n):
        sum_x += P[i][0]
        sum_y += P[i][1]
    sum_x /= n
    sum_y /= n
    return array([sum_x, sum_y])

#Перемещаем фигуру, заданную координатами P на вектор d
def move(P, d):
    return P + d

#Определяем матрицу (оператор) поворота по углу альфа:
def operatorP(alpha):
    return array([[cos(alpha), -sin(alpha)],
                  [sin(alpha), cos(alpha)]])

#Поворочиваем фигуру P на угол alpha относительно точки d:
def rotate(P, alpha, d):
    F=operatorP(alpha)
    print(F)
    print(P)
    return (P - d).dot(F) + d

#Изменяем размер фигуры P в k hfp относительно точки d:
def resize(P, k, d):
    return k*(P - d) + d

#Поворачиваем фигуру относительно её центра:
def rotateC(P, alpha):
    d = find_center(P)
    print(d)
    return rotate(P, alpha, d)

#Изменяем размер фигуры относительно её центра:
def resizeC(P, k):
    d = find_center(P)
    return resize(P, k, d)

#Устанавливаем размер холста (в дюймах) в зависимости от пропорций рамки R:
def sizedef(maxs, DPI, R):
    dx = abs(R[1][0] - R[0][0])
    dy = abs(R[1][1] - R[0][1])
    dmax = max(dx, dy)
    kx = dx/dmax
    ky = dy/dmax
    t = (kx*maxs/DPI, ky*maxs/DPI)
    print(t)
    return t

#Задаём фигуру (как список списков):
P = [[1,    1],
     [1,    -1],
     [-1,   -1],
     [-1,   1],
     [1,    1]]
#Преобразовываем список списков в матрицу numpy:
P = array(P)
print(P)
#Задаём рамку (левая нижняя граница холста и правая верхняя):
R=[[-5, -5],
   [25, 15]]
R = array(R)
#Количество точек на дюйм(?) - в норме от 80 до 120:
DPI = 120
#Максимальный размер холста в пикселях (либо по горизонтали, либо по вертикали, в зависимости от рамки):
max_s = 900
#Холст:
fig = figure(dpi=DPI, figsize=sizedef(max_s, DPI, R))
#Геометрическая фигура:
x = P[:, 0]
y = P[:, 1]
plot(x, y)
#Преобразованная геометрическая фигура:
P_new = P + array([5, 5])
P_new = rotateC(P, pi/4)
plot(P_new[:, 0], P_new[:, 1])
#Рамка:
ramka = plot(R[:, 0], R[:, 1])
#Делаем рамку невидимой (ширина линии = 0):
setp(ramka, linewidth=0)
#Параметры холста в ax:
ax = gca()
#Убираем верхнюю ось:
ax.spines['top'].set_color('none')
#Нижнюю ось - в начало координат:
ax.spines['bottom'].set_position('zero')
#Левую ось в начало координат:
ax.spines['left'].set_position('zero')
#Убираем правую ось:
ax.spines['right'].set_color('none')
#Отобразить холст:
show()


