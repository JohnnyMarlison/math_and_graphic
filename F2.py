from matplotlib.pyplot import *
from numpy import *
from matplotlib.animation import FuncAnimation

def closed_fig(P):
    return (P[0][0] == P[len(P) - 1][0]) and (P[0][1] == P[len(P) - 1][1])

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

    return [sum_x, sum_y]

def move(P, d):
    return P + d

def operatorP(alpha):
    return array([[cos(alpha), sin(alpha)],
                  [-sin(alpha), cos(alpha)]])

def rotate(P, alpha, d):
    F = operatorP(alpha)
    return (P - d).dot(F) + d

def resize(P, k, d):
    return k * (P - d) + d

def rotateC(P, alpha):
    d = find_center(P)
    return rotate(P, alpha, d)

def resizeC(P, k):
    d = find_center(P)
    return resize(P, k, d)

def sizedef(maxs, DPI, border):
    dx = abs(border[1][0] - border[0][0])
    dy = abs(border[1][1] - border[0][1])
    dmax = max(dx, dy)
    kx = dx / dmax
    ky = dy / dmax
    t = (kx * maxs / DPI, ky * maxs / DPI)
    print(t)
    return t

border = [[-6, -6], [6, 6]]
border = array(border)
DPI = 120
max_s = 900
fig = figure(dpi=DPI, figsize=sizedef(max_s, DPI, border))
rim = plot(border[:, 0], border[:, 1])
setp(rim, linewidth=0)

line, = plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    P = [[0, 0],
         [1, 1],
         [2, 0],
         [3, 1],
         [3, 2]]
    P = array(P)
    P = rotateC(P, pi * i / 90)
    x = P[:, 0]
    y = P[:, 1]
    line.set_data(x, y)
    return line,


if __name__ == '__main__':
    anim = FuncAnimation(fig, animate, init_func=init,
                            frames=200, interval=20, blit=True)
    ax = gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    show()
