from numba import njit
from numba import jit

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

print(pi_from_walles(10000000000))