# Вводится натуральное число n (то есть, целое положительное).
# В цикле перебрать все целые числа в интервале [1; n] и сформировать список из чисел,
# кратных 3 и 5 одновременно. Вывести полученную последовательность чисел в виде строки
# через пробел, если значение n меньше 100. Иначе вывести на экран сообщение
# "слишком большое значение n" (без кавычек).
# Использовать в программе оператор else после цикла while.

n = int(input())
i = 1
res = []

while i < n + 1:
    if n > 100 or n == 100:
        print("cлишком большое значение n")
        break
    if i % 3 == 0 and i % 5 == 0:
        res.append(i)
    i += 1
else:
    print(*res)

