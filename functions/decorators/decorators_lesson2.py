# Декораторы функций с параметрами
# Для того, чтобы в декоратор можно было добавить дополнительный параметр, необходимо декоратор обернуть в еще одну
# функцию

import math


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper

    return func_decorator


@df_decorator(dx=0.0000001)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)


# Чтобы сохранить имя __name__ и описание функции __doc__, нужно в декораторе прописать
# wrapper.__name__ = func.__name__
# wrapper.__doc__ = func.__doc__
#
# Чтобы это сделать силами языка и не писать постоянно это две строчки, можно сначала импортировать
# специальный декоратор
# from functools import wraps - встроенный декоратор
# Далее необходимо декорировать wrapper (декоратор) с параметром func:
# @wraps(func)
# def wrapper ...