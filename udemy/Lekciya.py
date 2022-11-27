"""
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f'an error occured: {ex}')
    except:
        print('unknown error occured!')
    except TypeError as ex:
            print(f'an error occured: {ex}')

c = divide(4, 2)
print(c)

c = divide(4, 0)
print(c)

divider = input()
c = divide(4, divider)
print(c)
"""

'''
class Character():
    pass


unit = Character()
print(type(unit))

""" Конструктор: """


class Character():
    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


unit = Character("Elf", 20, 40)
print(unit.race)
print(unit.damage)
print(unit.armor)


class Character:
    MAX_SPEED = 100
    dead_health = 0

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Character.dead_health


unit = Character("Ork")

unit.hit(20)
print(unit.is_dead())

print(unit.health)

unit.hit(80)
print(unit.is_dead())

'''

'''class Character:
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.damage = damage
        self.__race = race
        self._health = 100

        self.current_speed = 20

    def hit(self, damage):
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

c = Character('Elf')

    print(c.health)
    print(c.race)'''
'''
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)
'''

"""
a = 2
b = 5
a, b = b, a

print(a)
print(b)
"""

"""
Рекурсия
Должны быть(чтобыи збежать превышение объёма стека вызовов):
1. Рекуррентный случай
2. Крайний случай
"""

"""
def matryoshka(n):
    if n == 1:
        print('Матрешечка')
    else:
        print('верх матрешки n=', n)
        matryoshka(n - 1)
        print('Низ матрешки n=', n)


matryoshka(5)
"""
"""
Глубина рекурсии - количество вызовов функции
вводим параметр глубины рекурсии
"""

"""
  gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
  gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
  gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
  gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
"""
"""
import graphics as gr

window = gr.GraphWin('Russian game', 600, 600)
alpha = 0.1


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, deep - 1)


fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 100)
"""

