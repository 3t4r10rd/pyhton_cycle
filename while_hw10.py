# Вводятся два натуральных четных числа n и m в одну строчку через пробел,
# причем n < m. Напечатать все нечетные числа из интервала [n, m].
# Задачу решить без применения условного оператора.
# Результат вывести на экран в виде строки чисел, записанных через пробел.
# Программу реализовать при помощи цикла while.

n, m = map(int, input().split())

res = []
i = 1

while n <= m:

    res.append(n * (n %2))

    n += 1

while res.count(0):
    res.remove(0)


print(*res)