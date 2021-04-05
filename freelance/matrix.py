import numpy as np
# import random

def find_sum(matr):
    res = 0
    for str in matr:
        print(str)
        for i in range(len(matr)):
            # print(str[i])
            if str[i] > 0:
                res = 0
            elif str[i] < 0:
                res = sum(str)


        print(res)



matr = np.random.randint(-10, 50, (8, 8))
print(matr)
negsum = find_sum(matr)
