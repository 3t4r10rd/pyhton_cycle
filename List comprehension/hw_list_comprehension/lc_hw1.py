# На вход программе подаются вещественные числа, записанные через пробел.
# Необходимо их прочитать и сохранить в списке lst.
# Затем, используя list comprehension (генератора списков) сформировать новый список lst_abs
# из модулей чисел списка lst (в итоговом списке должны храниться именно числа, а не строки).
# Список lst_abs вывести на экран командой:
# print(*lst_abs)

lst = [float(x) for x in input().split()]
lst_abs = [abs(x) for x in lst]
print(*lst_abs)

# На вход программе подается семизначное целое положительное число.
# Необходимо его прочитать и с помощью list comprehension сформировать список lst,
# содержащий цифры этого числа (в списке должны быть записаны числа, а не строки).
# Полученный список вывести на экран командой:
# # print(lst)

a = int(input())

lst = [int(x) for x in str(a)]
print(lst)