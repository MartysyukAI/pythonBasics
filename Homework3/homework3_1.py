c = int(input('введите число'))
v = int(input('введите число отличное от нуля'))


def division(a, b):
    if b == 0:
        print('Делить на ноль нельзя')
    else:
        div = a / b
        print(div)


print(division(c, v))
