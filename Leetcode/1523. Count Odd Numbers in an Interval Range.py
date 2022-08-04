a = int(input('Enter a low positive number'))
b = int(input('Enter a high positive number'))
x = []
if 0 > a > b > 10**9:
    print('Enter a correct number')
elif a > b:
    print('Mixed up low and high number\nTry again')
else:
    for i in range(a, b+1):
        if i % 2 ==1:
            x.append(i)
print(len(x))
print(f'The odd numbers between {a} and {b} are {x}')