# Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n,
# которые кратны или 3 или 5. Результат (сумму) вывести на экран.
# Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.

n = int(input())
res = 0

for i in range(n):
    res += 0 if i % 3 and i % 5 else i

print(res)