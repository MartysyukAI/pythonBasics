limit = int(input('Enter the limit'))

for x in range(limit+1):
    if x % 2 == 0:
        print(f'{x} is EVEN')
    else:
        print(f'{x} is ODD')
