from matplotlib.pyplot import *
from numpy import *

p = [[1, 1],
     [2, 2],
     [3, 3],
     [2, 4]]
f = figure(dpi = DPI, figsize = (400 / DPI, 400/DPI))
p = plot(p[:, 0], p[:, 1])
setp(p, color = 'red', linewidth = 3)

show()
