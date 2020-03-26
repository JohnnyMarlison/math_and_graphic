import numpy as np

def printMatrix(matrix): 
   for i in range(len(matrix)): 
      for j in range(len(matrix[i])): 
          print("{:4d}".format(matrix[i][j]), end = "") 
      print()
      

matrix_1 = np.array([ [5, 6],
	[1, 1], 
	[5, 6] ])

matrix_2 = np.array([ [2, 2, 2],
	[2, 2, 2] ])

vector = np.array([ [5], [1] ])

mult_matr = matrix_1.dot(matrix_2)
mult_vec = matrix_1.dot(vector)

printMatrix(mult_matr)
print("\n")
printMatrix(mult_vec)