import numpy as np

def printMatrix(matrix): 
   for i in range(len(matrix)): 
      for j in range(len(matrix[i])): 
          print("{:4d}".format(matrix[i][j]), end = "") 
      print()

def sumMatrix(m1, m2):
	return m1 + m2

matrix_1 = np.array([[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],
    [1, 1, -1]])

matrix_2 = np.array([[1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],
    [1, 1, -1]])

print("First matrix:\n")
printMatrix(matrix_1)
print("\n")
print("Second Matrix:\n")
printMatrix(matrix_2)
print("\n")

print("Sum matrix:\n")
sum = sumMatrix(matrix_1, matrix_2)
printMatrix(sum)