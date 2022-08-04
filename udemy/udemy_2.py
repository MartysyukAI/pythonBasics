''' x1 = int(input('Enter x1'))
y1 = int(input('Enter y1'))
x2 = int(input('Enter x2'))
y2 = int(input('Enter y2'))

distance = round(((x1 - x2)**2 + (y1 -y2)**2)**0.5,3)
print(distance) '''

import math

x1 = int(input('Enter x1'))
y1 = int(input('Enter y1'))
x2 = int(input('Enter x2'))
y2 = int(input('Enter y2'))

distance = round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 3)
print(distance)

