import numpy as np
import random

# init matrix 4x13 with nums(1, 2, ... 53)
def init_matrix():
    matr = np.arange(1, 53).reshape((13, 4))
    return matr


def shuffle_matrix(matr):
    np.random.shuffle(matr)
    return matr

matr = init_matrix()
print("Martix:\n", matr)
shuf_matr = shuffle_matrix(matr) 
print("\n\n", "Shuffle matix:\n",shuf_matr)