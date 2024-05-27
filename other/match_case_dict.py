#Работа match/case со словорями и множествами

request = {'url': "http://...", "method": "GET", "timeout": 1000}

# Для словаря важно, чтоб присутствовали те элементы, которые мы проверяем.
# Если есть дополнительные элементы в словаре - ошибки не будет.
match request:
    case {'url': str() as url, "method": str(method)} if len(request) < 10: # заодно проверяем
                                                                            # тип значений в словаре и длинну словаря
        print(f"Запрос {url}, method {method}")
    case{"timeout": 1000}: # - проверяем точное значение ключа в словаре
        print(request["timeout"])

    case {"url": str(), **kwargs} if len(kwargs) == 2: # проверяем, что количество неиспользованных элементов = 2
        print ('kwargs')
    case {"url": str(), **kwargs} if not kwargs:  # проверяем, что не осталось незайдействованных ключей
        print('kwargs')
    case _:
        print("неверно")



keys = {1, 2, 3, 4}

match keys:
    case set() as k if len(k) == 3:
        print(k)
    case _:
        print("Ошибка")
