# Калькулятор
import numexpr
from colorama import init
from colorama import Fore
init()
print(Fore.CYAN)
expr = input('Введите математическое выражение')
result = numexpr.evaluate(expr)
print(Fore.GREEN)
print(f'Результат: {result}')
input()
