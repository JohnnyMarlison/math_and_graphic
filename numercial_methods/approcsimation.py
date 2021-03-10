import math

n = int(input('Введите степень многочлена: '))

print('Введите',n+1,'точек, через пробел в одну строку: ')
points = input().split()[:n+1]

print('Введите',n+1,'значений функций в этих точках:')
values = input().split()[:n+1]
flg = False
if values[1] == 'sin':
    for i in range(0,n+1,1):
        sin_x = math.sin(float(points[i]))
        values[i] = str(sin_x)
        flg = True
    m = float(input('Введите константу для оценки погрешности: '))

x = float(input('Введите точку в которой будем искать значение: '))

def proizv(x, i):
    res = 1
    for x_j in points:
        if points.index(x_j) != i:
            res *= ((x-float(x_j))/(float(points[i])-float(x_j)))
    return res

def lag(x):
    sum = 0
    for i in range(0,n+1,1):
        sum += (float(values[i])*proizv(x,i))
    return sum

if flg is True:
    omega = 1
    for x_j in points:
        omega *= (x - float(x_j))
    pogresh = m / math.factorial(n + 1) * math.fabs(omega)

print('Результат функции для точки ', x, ' равен:')
print(lag(x))
print()
if flg is True:
    print('Значение машинного синуса в заданной точке: ', math.sin(3.1415926535))
    print('Оценка погрешности: ', pogresh)







