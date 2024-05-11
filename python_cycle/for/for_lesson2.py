#Примеры
# enumerate(<список>) - пара + значение

# факториал
n = int(input())

if n < 1 or n > 100:
    print("Неверное число")
else:
    res = 1
    for i in range(1, n+1):
        res *= i
    print(f"Факториал равен {res}")

# лесенка из *
for i in range(1, 7):
    print("*" * i)


#объединить объекты из списка в одну строку

words = ['f','f','s','s']
s = ''
fl_First = True
for x in words:
    s += (' ' if fl_First else ' ') + x
    fl_First = False
print(s.lstrip())

# удалить из списка все двузначные числа

digs = [1, 2, 55, -75, 112, -7, -753]

for i, d in enumerate(digs):
    if 9 < abs(d) < 100:
        digs[i] = 0

print(digs)

# Преобразование кириллицы в латиницу

t = ['a', 'b', 'v', 'g', 'd']

start_index = ord("а")
title = "Абвгдэйка"
slug = ''

for s in title.lower():
    if 'а' <= s <= 'д':
        slug += t[ord(s)-start_index]
    else:
        slug += s

print(slug)
