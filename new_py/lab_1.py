# def make_pi():
#     q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
#     for j in range(1000):
#         if 4 * q + r - t < m * t:
#             yield m
#             q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
#         else:
#             q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


# my_array = []

# for i in make_pi():
#     my_array.append(str(i))

# my_array = my_array[:1] + ['.'] + my_array[1:]
# big_string = "".join(my_array)
# print "here is a big string:\n %s" % big_string
from math import factorial
from decimal import *

def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
        print("Step: {} of {}".format(k, n))
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi


N = 1000
getcontext().prec = N
val = chudnovsky(N / 14)
print(val)
# print()