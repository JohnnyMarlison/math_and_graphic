# Введите степень многочлена: 3
# Введите 4 точек, через пробел в одну строку: 
# 2.8 3.0 3.1 3.3
# Введите 4 значений функций в этих точках:
# sin sin sin sin
# Введите константу для оценки погрешности: 1
# Введите точку в которой будем искать значение: 3.1415926535
# Результат функции для точки  3.1415926535  равен:
# 9.697926367565474e-07

# Значение машинного синуса в заданной точке:  8.979318433952318e-11
# Оценка погрешности:  1.327791695455115e-05

from math import sin, factorial, fabs


def mult(x, i, points):
    res = 1
    for x_j in points:
        if points.index(x_j) != i:
            res *= ((x - float(x_j)) / (float(points[i]) - float(x_j)))
    return res


def lagranz(x, values, n, points):
    sum = 0
    pnts = points
    for i in range(0, n + 1, 1):
        sum += (float(values[i]) * mult(x, i, pnts))
    return sum


def main():
    n = int(input('Введите степень многочлена: '))
    
    print('Введите', n + 1,'точек, через пробел в одну строку: ')
    points = input().split()[:n + 1]
    
    print('Введите',n + 1,'значений функций в этих точках:')
    values = input().split()[:n + 1]
    flg = False
    if values[1] == 'sin':
        for i in range(0, n + 1, 1):
            sin_x = sin(float(points[i]))
            values[i] = str(sin_x)
            flg = True
        m = float(input('Введите константу для оценки погрешности: '))
    
    x = float(input('Введите точку в которой будем искать значение: '))
    
    if flg is True:
        omega = 1
        for x_j in points:
            omega *= (x - float(x_j))
        fault = m / factorial(n + 1) * fabs(omega)

    print('Результат функции для точки ', x, ' равен:')
    print(lagranz(x, values, n, points))
    print()
    if flg is True:
        print('Значение машинного синуса в заданной точке: ', sin(3.1415926535))
        print('Оценка погрешности: ', fault)

    
if __name__ == "__main__":
    main()