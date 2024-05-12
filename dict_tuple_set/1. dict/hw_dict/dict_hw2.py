# На вход программе поступают данные в виде набора строк в формате:
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN

# Ключами здесь выступают целые числа (см. пример ниже).
# В программе уже реализовано считывание всех строк и сохранение их в виде списка:

# lst_in = list(map(str.strip, sys.stdin.readlines()))

# Необходимо преобразовать список lst_in в словарь d (без использования функции dict())
# и вывести полученный словарь на экран командой:
# print(*sorted(d.items()))

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst = [lst_in[i].split('=') for i in range(len(lst_in))]

# решение 2
d1 = {}
for i in range(len(lst_in)):
    k, v = lst_in[i].split('=')
    d1[int(k)] = v
print(*sorted(d1.items()))

# решение 1
d = {}

for i in range(len(lst)):
    for j in range(len(lst[i])-1):
        d[int(lst[i][j])]=lst[i][j+1]

print(*sorted(d.items()))
