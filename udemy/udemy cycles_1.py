'''Вывести лесенкой символ звёздочки по кол-ву строк, заданных пользователем:
запросить ввод у пользователя кол-ва строк, вывести звёздочки лесенкой.
Например, пользователь ввёл число 2. Тогда выводим:
*
**
Например, пользователь ввёл число 4. Тогда выводим:
*
**
***
****
и так далее, смысл должен быть ясен
'''
rows = int(input('Enter the number of rows'))

for x in range(rows):
    print('*' * (x + 1))
