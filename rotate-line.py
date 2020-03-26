import pylab
import matplotlib.patches
import matplotlib.lines
import matplotlib.path


def drawLine (axes):
	x0 = 0
	y0 = 0
	x1 = 1
	y1 = 0.5

	x2 = 0.5
	y2 = 1.0

	line = matplotlib.lines.Line2D([x0, x1, x2], [y0, y1, y2], color="k")
	axes.add_line(line)

	pylab.text(0.5, 1.1, "Line2D", horizontalalignment="center")


if __name__ == "__main__":
	pylab.xlim(-2, 2)
	pylab.ylim(-2, 2)
	# pylab.grid()
	axes = pylab.gca()
	axes.set_aspect("equal")

	drawLine(axes)

	pylab.show()