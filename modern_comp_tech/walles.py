# Требуемая точность
# 3.1415926535
# Полученный результат с количеством 24050000000 повторений
# 3.141592653567845

from numba import njit

@njit(fastmath=True)
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


def main():
    count_iters = int(input())
    pi_w = pi_from_walles(count_iters)
    print("Walles: ", pi_w)
    pass

if __name__ == '__main__':
    main()