# Генераторы списков

# сгенерируем список квадратов числел от 0 до N с помощью цикла

N = 6
a = [0] * N

for i in range(N):
    a[i] = i ** 2

print(a)

#сделаем то же самое с помощью генератора списков

N = 6

a = [x** 2 for x in range(N)]

print(a)

#  синтаксис : [<способ формрования значения for <>переменная> in <итерируемый объект>]

# примеры:

# a = [1 for x in range(5)] (переенная x доступна только внутри генератора списков)
# [1, 1, 1, 1, 1]

# a = [x % 4 for x in range(6)]
# [0, 1, 2, 3, 0, 1]

# a = [x % 2 == 0 for x in range(6)]
# [True, False, True, False, True, False]

# a = [15 - x for x in range(5)]
# [15, 14, 13, 12, 11]

# a = [d for d in "python"]
# ['p', 'y', 't', 'h', 'o', 'n']

d_inp = input("Целые числа через пробел: ")

a = [int(d) for d in d_inp.split()]
print(a)


# в генераторах можно прописывать условия, составные условия

a = [x for x in range(-5, 5) if x < 0] #в списке значения только меньше 0
a = [x for x in range(-5, 5) if x % 2 == 0] # в списке только четные значения

# можно использовать совместно с тернарным оператор

d = [1, 2, 3, 4, 5]

a = ["четное" if x % 2 == 0 else "нечетное"
     for x in d
     if x > 0] # переберем числа в списке и выведем четные они или нет
               # в новый список для положительных числе
print(a)