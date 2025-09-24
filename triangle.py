from math import sqrt

a = int(input('введите 1 сторону треугольника '))
b = int(input('введите 2 сторону треугольника '))
c = int(input('введите 3 сторону треугольника '))

perim = a + b + c
p = perim / 2
# area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
area = sqrt(p * (p - a) * (p - b) * (p - c))

print(f'площадь равна  {area}  периметр равен  {perim}')