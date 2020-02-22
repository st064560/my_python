import math


def my_func(x):
    if 0.2 < x < 0.9:
        return math.sin(x)
    else:
        return 1

x = float(input('Введите значение x:'))
print(my_func(x))


