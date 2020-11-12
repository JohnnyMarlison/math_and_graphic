from math import *
from numba import njit

@njit
def pi_from_euler(count_iters):
    res_pi = 0
    for i in range(1, count_iters + 1):
        res_pi += (1 / (i * i))
    res_pi *= 6
    res_pi = sqrt(res_pi)
    return res_pi


@njit
def pi_from_walles(count_iters):
    res_pi = 1
    i = 0
    up = 2
    down = 1
    while i < count_iters:
        res_pi *= (up / down)
        if i % 2 == 0:
            down += 2
        else:
            up += 2
        i += 1
    res_pi *= 2
    return res_pi


@njit
def pi_from_viet(count_iters):
    res_pi = 1
    up = 0
    for i in range(count_iters):
        up = sqrt(2 + up)
        res_pi *= (up / 2)
    res_pi = 2 / res_pi
    return res_pi


@njit
def pi_from_madhava1(count_iters):
    res_pi = 0
    j = 1
    for i in range(count_iters):
        elem = (4 / j)
        if i % 2 == 1:
            elem *= (-1)
        res_pi += elem
        j += 2
    return res_pi


@njit
def pi_from_madhava2(count_iters):
    res_pi = 0
    for i in range(count_iters):
        res_pi += ((-1)**i * (1 / ((2 * i + 1) * 3**i)))
    res_pi *= sqrt(13)
    return res_pi


def main():
    count_iters = int(input())
    pi_e = pi_from_euler(count_iters)
    pi_w = pi_from_walles(count_iters)
    pi_v = pi_from_viet(count_iters)
    pi_m1 = pi_from_madhava1(count_iters)
    pi_m2 = pi_from_madhava2(count_iters)
    print("Euler: ", pi_e)
    print("Walles: ", pi_w)
    print("Viett: ", pi_v)
    print("Madhava1: ", pi_m1)
    print("Madhava2: ", pi_m2)
    pass

if __name__ == '__main__':
    main()
