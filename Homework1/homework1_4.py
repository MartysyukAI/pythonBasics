#  Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.

def bigest_number(input_number):
    if input_number <= 0:
        return 'Введите целое положительное число'
    iter = 0
    bigest_number = 0
    while iter < len(str(input_number)):
        if int(str(input_number)[iter]) > bigest_number:
            bigest_number = int(str(input_number)[iter])
        iter += 1
    return bigest_number


input_number = int(input('Введите целое положительное число: '))
print(bigest_number(input_number))
