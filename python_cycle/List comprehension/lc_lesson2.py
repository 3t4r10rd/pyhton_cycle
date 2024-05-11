# вложенные генераторы списков

a = [(i, j)
     for i in range(3) if i % 3 ==0
     for j in range(4) if j % 2 == 0
     ]
print(a)


b = [f"{i}*{j} = {i*j}"
     for i in range(3)
     for j in range(4)
     ]
print(b)


matrix = [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23]]
c = [x
     for row in matrix
     for x in row
     ]
print(c)

M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# возводит в квадрат и возвращает такой же вложенный список
d = [[x ** 2 for x in row] for row in A]
print(d)
# возводит в квадрат и возвращает все значения в одномерном списке
d1 = [x ** 2
      for i in A
      for x in i
      ]
print(d1)


g = [u ** 2 for u in [x + 1 for x in range(5)]]
print(g)