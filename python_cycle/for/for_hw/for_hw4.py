# Вводится натуральное число n. С помощью цикла for найти все делители этого числа.
# Найденные делители выводить сразу в столбик без формирования списка.

x = int(input())

for i in range(1, x+1):
    if x % i == 0:
        print(i)