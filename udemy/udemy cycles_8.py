import random

tries = 0

number = random.randint(1, 50)

print('Try to guess what number between 1 and 50')

while tries < 6:
    guess = int(input('take a guess:'))
    tries += 1

    if guess == number:
        print('you win')

    elif guess > number:
        print('<')
    elif guess < number:
        print('>')
