import numpy as np

def find_k(matr):
    k = 0
    for i in range(len(matr)):
        if matr[i].any() == matr[:,i].any():
            k = i + 1

    print(k)


def find_sum(matr):
    res = 0
    for str in matr:
        for i in range(len(matr)):
            if str[i] < 0:
                res = sum(str)
                break
            else:
                res = 0
                continue


        print("String", str, "Sum = ", res)


def main():
    # matrix for other
    # matr = np.random.randint(-10, 50, (4, 4))   
    # matrix for example
    matr = np.array([
        [1, 2, 3, -4, 5, 6, 7, 8],
        [2, 3, -4, 5, 6, 7, 8, 9],
        [3, -4, -5, 6, 7, 8, 9, 10],
        [-4, 5, 6, 7, 8, 9, 10, 11],
        [5, 6, 7, 8, 9, 10, 11, 12],
        [6, 7, 8, 9, 10, 11, 12, 13],
        [7, 8, 9, 10, 11, 12, 13, 14],
        [8, 9, 10, 11, 12, 13, 14, 15]

    ])

    print(matr)

    print("\nFind Sum elems in string if have negative elem:\n")
    find_sum(matr)
    
    print("\nFind k:")
    find_k(matr)


if __name__ == "__main__":
    main()