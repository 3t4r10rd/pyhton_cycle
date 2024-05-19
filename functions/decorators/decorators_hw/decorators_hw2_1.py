    # На вход программе подаются целые числа, записанные через пробел.
# Прочитайте эту строку и сохраните через какую-либо переменную.
#
# Напишите функцию, которая имеет один параметр, преобразовывает переданную ей строку в список чисел
# и возвращает их сумму.
#
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для прочитанной строки.
# Результат (сумму) отобразите на экране.


def decorator_start(start=0):
    def decorator_sum(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start

        return wrapper
    return decorator_sum
@decorator_start(start=5)
def get_numbers(numbers):
    return sum([int(i) for i in numbers.split()])


nums = input()

print(get_numbers(nums))