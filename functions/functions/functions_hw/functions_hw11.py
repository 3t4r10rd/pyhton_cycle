# На вход программе подаются целые числа, записанные через пробел.
# Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку этого списка по возрастанию
# с помощью алгоритма сортировки слиянием. Функция должна возвращать новый отсортированный список.
#
# Вызовите результирующую функцию сортировки для введенного списка и отобразите
# результат на экран в виде последовательности чисел, записанных через пробел.
#
# Подсказка: для разбиения списка и его последующей сборки используйте рекурсивные функции.

numbers = list(map(int, input().split()))

def get_sl(a, b):
    c = []
    N = len(a)
    M = len(b)
    i = 0
    j = 0

    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    print(c)
    return c


#
def get_sort(n):
    a, b = [], []
    for i in range(len(n)):
        a.append(n[i]) if i <= (len(n) // 2) - 1 else b.append(n[i])
    # check_a = 2 if len(a) % 2 else 1
    # check_b = 2 if len(b) % 2 else 1

    if len(a) > 1:
        a = get_sort(a)

    if len(b) > 1:
        b = get_sort(b)



    return get_sl(a, b)

print(*get_sort(numbers))