# На вход программе поступает строка с вещественными числами, записанными через пробел. Необходимо прочитать эту строку.
# Затем, с помощью функции map преобразовать числа в строке в их вещественное представление и отобразить
# первые три числа. (Полагается, что минимум три вещественных числа имеются).
# Реализовать извлечение чисел через функцию next. Результат отобразить в строчку через пробел.

s = map(float, input().split())

for x in range(3):
    print(next(s), end=" ")

# На вход программе поступает строка из целых чисел, записанных через пробел. Необходимо прочитать эту строку.
# Затем, с помощью функции map преобразовать эту строку в список целых чисел, взятых по модулю.
# Сформируйте именно список lst из таких чисел. Отобразите его на экране командой:
#
# print(*lst)


a = input().split()
lst = list(map(abs, map(int, a)))
print(*lst)
# или через лямбда функцию
a = input().split()
lst = list(map(lambda x: abs(int(x)), a))
print(*lst)