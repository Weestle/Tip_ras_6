def disp(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('%-7s' % matrix[i][j], end="")
        print()


def mult_vecnum(n, vec):
    temp = [0] * len(vec)
    for i in range(len(vec)):
        temp[i] = vec[i] * n
    return temp


def mult_matmat(mat1, mat2):
    l = len(mat1)
    m = len(mat1[0])
    n = len(mat2[0])
    res = []

    for i in range(len(mat1)):
        tmp = [0] * n
        res.append(tmp)

    for i in range(l):
        for j in range(n):
            s = 0
            for r in range(m):
                s += mat1[i][r] * mat2[r][j]
            res[i][j] = s

    return res


def gauss(SLAU):
    SIZE = len(SLAU)

    # Вся магия происходит тут
    for i in range(SIZE):
        SLAUii = SLAU[i][i]
        line = []
        for j in range(i + 1, SIZE):
            line.append(SLAU[j][i])
        for j in range(i, SIZE + 1):
            SLAU[i][j] /= SLAUii
            for k in range(i + 1, SIZE):
                SLAU[k][j] -= line[(k - 1 + len(line)) % len(line)] * SLAU[i][j] / SLAU[i][i]
        # disp(SLAU)

    # Подсчет иксов
    X = [0] * SIZE
    for i in range(SIZE - 1, -1, -1):
        s = 0
        for j in range(i + 1, SIZE):
            s += SLAU[i][j] * X[j]
        X[i] = SLAU[i][SIZE] - s

    for i in range(SIZE):
        X[i] = round(X[i], 2)

    return X


def eigenvalues(matrix):
    l = len(matrix)

    # y = []
    # for i in range(l):
    #     tmp = [1]
    #     y.append(tmp)

    y = [[0], [1]]

    for i in range(l):
        tmp = []
        for j in range(l):
            tmp1 = []
            tmp1.append(y[j][i])
            tmp.append(tmp1)
        a = mult_matmat(matrix, tmp)
        for i in range(l):
            y[i].append(a[i][0])
    disp(y)

    for i in range(l):
        tmp = y[i][0]
        y[i][0] = y[i][1]
        y[i][1] = tmp
        y[i][len(y)] *= -1

    print(gauss(y))



a = [
    [4, 2],
    [0, 3]
]

# a = [
#     [4, -3, 3],
#     [1, 2, 1],
#     [1, 1, 2]
# ]

eigenvalues(a)
