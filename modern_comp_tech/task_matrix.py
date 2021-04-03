# Путем перестановки элементов квадратной вещественной матрицы добиться того, чтобы ее максимальный элемент находился в левом верхнем углу (1,1), 
# следующий по величине – в позиции (2, 2), следующий по величине – в позиции (3, 3) и т. д., заполнив, таким образом, всю главную диагональ. 
# Найти 	номер 	первой 	из 	строк, 	не 	содержащих 	ни 	одного положительного элемента. 


import random
import copy
from module_matrix import *


def main():
    print("Enter square matrix size: ")
    n = int(input())
    matrix = [[round((random.uniform(-100,100)), 3) for i in range(n)] for j in range(n)] 
    print("matrix:\n", matrix)
    print(len(matrix))
    new_matr = max_diagonal(matrix)
    print("matrix with max diagonal:\n", new_matr)
    row = find_negative_row(matrix)
    print("number first negative row:\n", row)



if __name__ == "__main__":
    main()
