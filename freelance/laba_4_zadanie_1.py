from math import sqrt
import turtle as tr
aX = [-7, 3]
aY = [-1, 2]
Dx = 800
Dy = Dx / ((aX[1]- aX[0]) / (aY[1]- aY[0]))
tr.setup(Dx, Dy)
Nmax = 1000
tr.setworldcoordinates(aX[0], aY[0], aX[1],
aY[1])
def MyFun(xt):
    if (xt >=3 ) and (xt <= -7):
        return(None)
    if xt < -6:
        y=1
    elif xt >=-6 and xt<-4:
        y= -(1/2)*xt-2
    elif xt >= -4 and xt<0:
        y=sqrt(4-(xt+2)**2)
    elif xt >= 0 and xt<2:
        y=-1*sqrt(1-(xt-1)**2)
    elif xt >= 2 and xt<3:
        y=-xt+2
    return (y)


def osi():
    tr.speed(20)
    tr.up()
    tr.goto(-7,0)
    tr.down()
    tr.goto(3, 0)
    tr.up()
    tr.goto(0,-1)
    tr.down()
    tr.goto(0,2)
    tr.up()

osi()
def delenie():
    tr.speed(20)
    tr.goto(-7,0)
    tr.up()
    for i in range(-7,4,1):
        tr.goto(i,0)
        tr.down()
        tr.goto(i,-0.2)
        tr.up()
        tr.goto(i,0)
        tr.down()
        tr.goto(i,0.2)
        tr.up()
        tr.write(i)
    for i in range(-1,3,1):
        tr.goto(0,i)
        tr.down()
        tr.goto(0.2,i)
        tr.up()
        tr.goto(0,i)
        tr.down()
        tr.goto(0.2,i)
        tr.up()
        tr.write(i)
delenie()
tr.width(5)
tr.color("red")
dx = (aX[1] - aX[0])/Nmax
tr.goto(-7,1)
tr.up()
tr.down()
xt=-7
xe=3
while xt <= xe:
    tr.down()
    tr.goto(xt,MyFun(xt))
    xt+=0.1

tr.done()


