import random
import copy


def find_negative_row(matr):
    i = 0
    j = 0
    res = 0
    tmp = 0
    while i < len(matr):
        row = matr[i]
        for j in range(len(matr)):
            if row[j] < 0:
                tmp += 1
                res = i
                if tmp == len(matr) - 1:
                    return res
            else:
                j = 0
                res = 0
                tmp = 0
                i += 1

    return None

def max_diagonal(arr):
    max_vals = []
    tmp_matr = copy.deepcopy(arr)
    min_num = -100000000000
    for c in range(len(tmp_matr)): 
        tmp_max = (min_num, 0, 0)
        for i in tmp_matr:
            if max(i) > tmp_max[0]:
                tmp_max = (max(i), tmp_matr.index(i), i.index(max(i)))
        max_vals.append((tmp_max[0], tmp_max[1], tmp_max[2]))
        # idx_max.append(())
        tmp_matr[tmp_max[1]][tmp_max[2]] = min_num
    print(max_vals)

    for i in range(len(arr)):
        arr[i][i], arr[max_vals[i][1]][max_vals[i][2]] = arr[max_vals[i][1]][max_vals[i][2]], arr[i][i]

    return arr
