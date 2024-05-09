
#break - досрочное завершение цикла
#continue - пропуск одной итерации цикла
#else в цикле while - блок, выполняемый после ШТАТНОГО завершения цикла while

#
d = [1, 5, 3, 67, 503, -43]
flFind = False
i = 0
while i < len(d):
    flFind = d[i] % 2 == 0
    if flFind:
        break

    i += 1

print(flFind)



#суммируем все нечетные значения до ввода 0
s = 0
a = 1

while a != 0:
    a = int(input("Введите целое число: "))
    if a % 2 == 0:
        continue

    s += a
    print("s = " + str(s))



#S = 1/2 + 1/3 + 1/4 + 1/10 + ... , пока не будет деления на 0

k = 0
l = -10

while l < 10:
    if l == 0:
        break
    k += 1/l
    l += 1
else:
    print("Сумма вычислена корректно")

print(k)