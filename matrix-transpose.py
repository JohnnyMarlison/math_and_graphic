import numpy as np

def printMatrix(matrix): 
   for i in range(len(matrix)): 
      for j in range(len(matrix[i])): 
          print("{:4d}".format(matrix[i][j]), end = "") 
      print()

matrix = np.array([[1, -1], 
	[2, -2], 
	[3, -3]])
printMatrix(matrix)

matr_transpose = matrix.transpose()
printMatrix(matr_transpose)