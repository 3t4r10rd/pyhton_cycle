# Команды match/case позволяют проверять переменню на соответствие шаблонам
#
# match <переменная>:
#     case <шаблон 1>:
#         список команд
#     ...
#     case <шаблон N>:
#         список команд
#     case <переменная>>:
#         список команд, если ни один case не подошел, при этом переменной присваивается значение переменной из case

# cmd = "top"
#
# match cmd:
#     case "top" | "вверх":
#         print("вверх")
#     case "right":
#         print("вправо")
#     case _:
#         print('не подошло')


# Если в case указать новую переменную, то она будет ссылаться на то же значение, что и переменная в match

# cmd = "right"
# match cmd:
#     case commamd:
#         print(commamd)

#
# cmd = "right"
# match cmd:
#     case str(): # проверка, является ли cmd строкой
#         print(cmd)
#
cmd = "right"
match cmd:
    case str() as command: # если cmd имеет тип строка, то создается переменная command, ссылающаяся на строку cmd
        print(command)
    case int() | float() as command if 0 <= command <= 5: # проверяем на типы int/float - если да, то проверяем условие
        print(command)