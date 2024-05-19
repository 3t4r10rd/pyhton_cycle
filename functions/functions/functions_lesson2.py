# Через return указывается, что функция будет возвращать
# Внутри функции можно указывать только ОДИН оператор return
# После оператора return функция прекращает работу
# Если необходимо вернуть 2 переменные, то можно вернуть кортеж (a, b) или любую коллекцию

def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res, x

def get_max2(a, b):
    return a if a > b else b

# в функциях можно использовать ранее объявленные функции

def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))

# можно объявить функцию в циклах
PERIMETR = True
if PERIMETR:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect (a, b):
        return a * b


def even(x):
    return x % 2 == 0

a, b = get_sqrt(49)
print(a, b)

# функции можно использовать с рекурсией
print(get_max2(5, get_max2(7, 10)))
print(get_max3(5, 7, 11))

for i in range(1, 19):
    if even(i):
        print(i, end=" ")