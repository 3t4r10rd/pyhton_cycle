# Повторите задачу с транспонированием прямоугольной матрицы
# с помощью list comprehension, изложенной в видео-уроке к этой практике.
# На вход программе поступает таблица целых чисел, чтение которой уже реализовано в программе:

# Sample Input:
# 1 2 3
# 4 5 6
# 7 8 9
# 5 4 3

# Sample Output:
# 1 4 7 5
# 2 5 8 4
# 3 6 9 3
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

A = [
    [ i[j]
     for i in lst_in
    ]
    for j in range(len(lst_in[0]))
]




for row in A:
    print(*row)



