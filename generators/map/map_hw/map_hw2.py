#  На вход программе подается таблица целых чисел. Строки этой таблицы уже в программе читаются командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Далее, используя функцию map и генератор списков, преобразуйте список строк lst_in в двумерный (вложенный) список
# с именем lst2D, содержащий целые числа (а не их строковое представление).
#
# Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

def gen(lst):
    for i in range(len(lst)):
        res = []
        for j in lst[i].split():
            res.append(int(j))
        yield res


a = gen(lst_in)

lst20 = list(map(list, a))

print(lst20)

# ИЛИ

lst2D = [list(map(int, i.split())) for i in lst_in]
print(lst2D)