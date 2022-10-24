num = int(input('Enter the number'))

original_num = num
reversed_num = 0

while original_num > 0:
    reversed_num = (reversed_num * 10) + original_num % 10
    original_num = original_num // 10

if num == reversed_num:
    print('Palindrom')
else:
    print('No Palindrom')
