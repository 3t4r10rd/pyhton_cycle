#Вводится строка (слаг). Замените в этой строке все
# подряд идущие дефисы (--, ---, ---- и т.д.) на одинарные (-).
# Результат преобразования строки выведите на экран.
# Программу реализовать при помощи цикла while.


#через списки
word = input()

lst = list(word)

while "--" in word:
    lst.pop(word.find("--"))
    word = "".join(lst)

print(word)

#через replace

word2 = input()

while "--" in word2:
    word2 = word2.replace("--", "-")

print(word2)