# сформируем треугольник Паскаля
#                 [ [1],
#                 [1, 1],
#               [1, 2, 1],
#              [1, 3, 3, 1],
#             [1, 4, 6, 4, 1] ]


N = 7 # glubina treugolnika
P = [] # treugolnik

for i in range(N-1):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]

    P.append(row)

for r in P:
    print(r)