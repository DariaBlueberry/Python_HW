# Площадь квадрата
import math


def square(x):
    return math.ceil(x * x)


b = int(input('Какая длина стороны квадрата?'))
result = square(b)
print(f'Площадь квадрата равна {result}.')
