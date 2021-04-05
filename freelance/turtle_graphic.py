from turtle import *
from turtle import setup as st

aX = [-7, 12]
aY = [-3.5, 3.5]
Dx = 800
Dy = Dx / ((aX[1] - aX[0]) / (aY[1] - aY[0]))
st(Dx, Dy)
Nmax = 1000
setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

def MyFunc():
    up()
    width(5)
    color("black")
    dx = (aX[1] - aX[0])/Nmax
    goto(-7, 3)
    up()
    down()
    goto(-3, 3)
    up()
    down()
    right(90)

    for i in range(93):
        left(1.9)
        forward(0.1)

    goto(6, -3)
    goto(11, 2)

def coordinate_axis():
    speed(20)
    up()
    goto(-7,0)
    down()
    goto(12, 0)
    up()
    goto(0,-3)
    down()
    goto(0,3)
    up()

def numerical_marks():
    speed(20)
    goto(-7,0)
    up()
    for i in range(-7,12,1):
        goto(i,0)
        down()
        goto(i,-0.2)
        up()
        goto(i,0)
        down()
        goto(i,0.2)
        up()
        write(i)
    for i in range(-3,4,1):
        goto(0,i)
        down()
        goto(0.2,i)
        up()
        goto(0,i)
        down()
        goto(0.2,i)
        up()
        write(i)


def main():
    coordinate_axis()
    numerical_marks()
    MyFunc()
    done()

if __name__ == "__main__":
    main()
