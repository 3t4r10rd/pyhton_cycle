# Декораторы функций
# # декорирование можно сделать либо
# <имя функции> = <функция декоратор>(<имя функции>)
# либо перед объявлением декорируемой функции постаить @<функция декоратор>



def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("----действия до функции----")
        res = func(*args, **kwargs)
        print("---действия после функции----")
        return res

    return wrapper

@func_decorator
def some_func():
    print("вызов функции")

# some_func = func_decorator(some_func)
some_func()