# for <переменная> in <итерируемый объект>:
#    ...
#    ...
# range(start, stop, step)
# range(start, stop)
# range(stop)

d = [1, 2, 3, 4, 5]

for x in d:
    print(x)


for x in "python":
    print(x)


for i in range(len(d)):
    d[i] = 0

print(d)

