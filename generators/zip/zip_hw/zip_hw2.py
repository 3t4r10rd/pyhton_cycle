# На вход программе подается строка из слов, записанных через пробел. Необходимо прочитать эту строку,
# разбить на слова на основе полученного списка составить прямоугольную таблицу из трех столбцов и N строк
# (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
# Реализовать эту программу с использованием функции zip. Результат отобразить на экране
# в виде прямоугольной таблицы из слов, записанных через пробел (в каждой строчке).

lst = input().split()

N = len(lst) // 3
res = [lst[:3], lst[3:6], lst[6:]]

z = zip(*zip(*res))

for i in z:
    print(*i)

