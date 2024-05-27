# Функция служит для фильтрации элементов итерированного объекат
#
# filter(func, *iterables) - если для текущего элемента func == True, то эначение возвращается функции filter
# Если False - то значение пропускается

# Является ли число четным
a = [1, 2, 3, 4, 5]

b = filter(lambda x: x % 2 == 0, a)
lst = list(b)
print(lst)

# Является ли число простым или нет

def is_simple(x):
    d = x - 1
    if d < 0:
        return False

    while d > 1:
        if x % d == 0:
            return False

        d -= 1

    return True

b2 = filter(is_simple, a)
lst2 = tuple(b2)
print(lst2)


# В функцию filter в качестве перебираемого объекта можно указать другую функцию filter
#
# b = filter(func, filter(func2, a))

d = filter(lambda x: x % 2 != 0, filter(is_simple, a))
print(list(d))