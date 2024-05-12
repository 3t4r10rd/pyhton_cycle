# На вход программе поступают номера телефонов с привязкой к именам в виде строк
# следующего формата:
#
# номер_1 имя_1
# номер_2 имя_2
# ...
# номер_N имя_N
#
# В программе уже реализовано считывание всех строк и сохранение их в виде списка:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# На основе списка lst_in необходимо создать словарь d,
# где ключами будут имена, а значениями - список номеров телефонов для этого имени (ключа).
# Обратите внимание, что одному имени может принадлежать несколько разных номеров.
# Полученный словарь вывести командой:
# print(*sorted(d.items()))

import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['+71234567890 Сергей', '+71234567810 Сергей', '+51234567890 Михаил', '+72134567890 Николай']


# простой метод

# d = {}
#
# for i in lst_in:
#     values, keys  = i.split()
#
#     if keys not in d:
#         d[keys] = [values]
#     else:
#         d[keys] += [values]



# мое решение

keys = []
values = []
d = {}

for i in lst_in:
    keys.append(i.split()[1])
    values.append([])
    values[lst_in.index(i)].append(i.split()[0])

for i in range(len(keys)):
    if keys[i] not in d:
        d[keys[i]] = values[i]
    else:
        d[keys[i]].append(values[i][0])

print(*sorted(d.items()))



