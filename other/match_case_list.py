# # Можно использовать для кортежей и для списков
#
# cmd = ('автор', "книга", 2000)
#
# match cmd:
#     case tuple() as book:
#         print(f"кортеж {book}")
#
# cmd = ('автор', "книга", 2000, 1, 2, 3)
# # Можно сразу распаковать кортеж
# match cmd:
#     case author, title, price: # сработает только в случае, когда в кортеже 3 элемента
#         print(f"кортеж {author}, {title}, {price}")
# # сработает с любым размером кортежа и списка
#     case author, title, price, *other: # первые 3 запишутся в 3 переменные, в others запишется все остальное
#         print((f"кортеж {author}, {title}, {price}"))
#
# # Можно использовать условные операторы, например, if len(cmd) == 3
#     case author, title, price if len(cmd) == 3: # первые 3 запишутся в 3 переменные, если в кортеже их 3
#         print((f"кортеж {author}, {title}, {price}"))
#
# # Можно проверить тип данных объектов внутри кортежа
#     case str() as author, str() as title, float() as price: # работает только при совпадении типа данных
#         print((f"кортеж {author}, {title}, {price}"))


