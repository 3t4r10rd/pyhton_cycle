# Тестовый веб-сервер возвращает HTML-страницы по URL-адресам (строкам).
# На вход программе поступают различные URL-адреса, записанные каждое с новой строки.
# В программе уже реализовано считывание всех строк и сохранение их в виде списка:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Необходимо перебрать в цикле этот список с URL-адресами и если адрес появился
# (пришел) впервые, то на экране отобразить строку (без кавычек):
#
# "HTML-страница для адреса <URL-адрес>"
#
# и сохранить в словаре эту строку с ключом текущего URL-адреса.
# Если же URL-адрес встречается (приходит) повторно (проверяется по ключам словаря),
# то следует взять строку "HTML-страница для адреса <URL-адрес>" из этого словаря
# и вывести на экран сообщение (без кавычек):
#
# "Взято из кэша: HTML-страница для адреса <URL-адрес>"
#
# Сообщения выводить каждое с новой строки.
#
# P.S. Подобные задачи на практике решаются через хэш-таблицы.
# В Python словарь - это хэш-таблица. Скорость поиска ключа в нем выполняется очень быстро
# (намного быстрее, чем в списке). Именно поэтому решать ее через список очень плохая практика.

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {}

for i in lst_in:

    if i not in d:
        d[i] = f"HTML-страница для адреса {i}"
        print(d[i])



    else:
        print(f"Взято из кэша: {d[i]}")
