# # Функция map
#
# b = map(int, ['1', '2', '3']) - функция возвращает генератор(итератор) из элементов списка с применением функции int
# b = (int(x) for x in ['1', '2', '3']) - то же самое
#
# Функция map последовательно применяет функцию int к каждому элементу
# Можно прописывать вместо int любую функцию, которая принимает один аргумент и возвращает какое-то значение
# Например, len, str.upper и т.д.
#
# Так же можно указывать свои функции, в том числе и lambda функции

cities = ['Москва', 'Астрахань', 'Самара']
b = map(lambda x: list(x.lower()), cities)

print(list(b))







