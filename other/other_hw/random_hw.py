import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)

def is_ok(i, j):
    res = True
    check_list = [0]
    if P[i][j] == 1:
        res = False
    if i == 0:
        # print(1)
        if j == 0:
            # print(2)
            check_list = [P[i][j], P[i][j + 1], P[i + 1][j], P[i + 1][j + 1]]
        elif j == N -1:
            # print(3)
            check_list = [P[i][j], P[i][j - 1], P[i + 1][j - 1], P[i + 1][j]]
        else:
            # print(4)
            check_list = [P[i][j], P[i][j - 1], P[i][j + 1], P[i + 1][j - 1], P[i + 1][j], P[i + 1][j + 1]]
    elif i == N-1:
        # print(5)
        if j == 0:
            # print(6)
            check_list = [P[i][j], P[i][j + 1], P[i - 1][j], P[i - 1][j + 1]]
        elif j == N -1:
            # print(7)
            check_list = [P[i][j], P[i][j - 1], P[i - 1][j - 1], P[i - 1][j]]
        else:
            # print(8)
            check_list = [P[i][j], P[i][j - 1], P[i][j + 1], P[i - 1][j - 1], P[i - 1][j], P[i - 1][j + 1]]
    elif i != (0, N-1) and j == 0:
        # print(9)
        check_list = [P[i][j], P[i][j + 1], P[i - 1][j], P[i - 1][j + 1], P[i + 1][j], P[i + 1][j + 1]]
    elif i != (0, N-1) and j == N-1:
        # print(10)
        check_list = [P[i][j], P[i][j - 1], P[i - 1][j], P[i - 1][j - 1], P[i + 1][j], P[i + 1][j - 1]]
    else:
        # print(11)
        check_list = [P[i][j], P[i][j-1], P[i][j+1], P[i-1][j-1], P[i-1][j], P[i-1][j+1], P[i+1][j-1], P[i+1][j], P[i+1][j+1]]


    if max(check_list) == 1:
        res = False

    # print(check_list)
    # print(res)
    return res




N = 7 #int(input())
P = [[0] * N for i in range(N)]

M = 10
one = [1] * M

while one:
    i = random.randint(0, N-1)
    j = random.randint(0, N-1)
    if is_ok(i,j):
        P[i][j] = one.pop()

# for i in P:
#    print(*i)