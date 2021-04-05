
from math import sqrt
x = float(input('Введите значение x='))
if x <=-3:
  y=3
elif x >-3 and x<=3:
  y=3-sqrt(9-(2**x))
elif x>3 and x<=6:
  y=-2*x+9
else:
  y=x-9
print("X={0:.2f} Y={1:.2f}".format(x, y))
