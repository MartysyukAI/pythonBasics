Num = int(input('Enter the number'))

total_sum = 0
for x in range(Num + 1):
    if x % 3 == 0 or x % 5 == 0:
        total_sum += x
    else:
        continue

print(f'total sum = {total_sum}')


limit = int(input('Enter the limit'))

total_sum = sum([x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0])

print(f'total sum = {total_sum}')





num = int(input('Enter the num'))

sum([i for i in range(num) if i % 3 == 0 or i % 5 == 0])










