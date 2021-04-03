# В одномерном массиве, состоящем из n вещественных элементов, вычислить: 
#     1. Сумму положительных элементов. 
#     2. Число элементов, расположенных между максимальным по модулю и минимальным по модулю элементами. 
#     3. Упорядочить элементы массива по убыванию. 

import random
from math import *

def get_sum(arr, n):
    # print("Sum :")
    i = 0
    sum_arr = 0
    while i < n:
        if arr[i] > 0:
            sum_arr += arr[i]
            i += 1
        else:
            i += 1 
    
    return sum_arr


def count_elem(arr):
    a = list(arr)
    val_min, idx_min = min((abs(val_min), idx_min) for (idx_min, val_min) in enumerate(a))
    val_max, idx_max = max((abs(val_max), idx_max) for (idx_max, val_max) in enumerate(a))
    
    if idx_max > idx_min:
        return idx_max - idx_min
    else:
        return idx_min - idx_max

def sort_arr(arr):
    a = list(arr)
    a.sort(reverse = True)
    return a


def main():
    random.seed()
    print("Enter array size: \n")
    n = int(input())
    arr = [random.uniform(-100.0, 100.0) for r in range(n)]
    print(arr, "\n")
    sum_arr = get_sum(arr, n)
    print("Sum positive elements: ", sum_arr, "\n")
    res = count_elem(arr)
    print("The number of elements located between the maximum in modulus and minimum in modulus: ", res)
    sorted_arr = sort_arr(arr)
    print("\n")
    print("Sort array elements in descending order", sorted_arr, "\n")

    # print(arr)


if __name__ == "__main__":
    main()