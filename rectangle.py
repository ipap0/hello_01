length = int(input('введите длину прямоугольника '))
width = int(input('введите ширину прямоугольника '))
if length <0 or width <0:
    print("отрицательная длина или ширина")
else:
    perim = 2 * (length + width)
    area = length * width

    print('площадь равна ', area, ' периметр равен ', perim)
    print(f'площадь равна  {area}  периметр равен  {perim}')