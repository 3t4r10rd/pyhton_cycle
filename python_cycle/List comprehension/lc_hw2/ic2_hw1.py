# На вход программе подается двумерная таблица из целых чисел (см. пример ниже).
# В программе уже реализовано его чтение и сохранение в двумерном списке:
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# С помощью list comprehension необходимо преобразовать двумерный список lst_in
# в одномерный так, чтобы значения элементов шли в обратном порядке.
# Результат отобразить в виде строки из чисел, записанных через пробел.

# 1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2

import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst = [
        [x for x in y[::-1]]
        for y in lst_in[::-1]
      ]

#lst = [
#       [lst_in[i][j] for j in range(len(lst_in[i])-1, -1, -1) ]
#       for i in range(len(lst_in)-1, -1, -1)
#      ]

lst = [x for row in lst for x in row]

print(*lst)