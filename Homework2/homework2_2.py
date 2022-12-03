# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

my_list = [i for i in input('Введите любое количество цифр через пробел: ').split()]
"""
idx = 0
if len(my_list) % 2 == 0:
    while idx < len(my_list):
        temp = my_list[0 + idx]
        my_list[0 + idx] = my_list[1 + idx]
        my_list[1 + idx] = temp
        idx += 2
else:
    while idx < len(my_list) - 1:
        temp = my_list[0 + idx]
        my_list[0 + idx] = my_list[1 + idx]
        my_list[1 + idx] = temp
        idx += 2

print(my_list)
"""
idx = 0
if len(my_list) % 2 == 0:
    while idx < len(my_list):
        my_list[0 + idx], my_list[1 + idx] = my_list[1 + idx], my_list[0+idx]
        idx += 2
else:
    while idx < len(my_list) - 1:
        my_list[0 + idx], my_list[1 + idx] = my_list[1 + idx], my_list[0+idx]
        idx += 2

print(my_list)
