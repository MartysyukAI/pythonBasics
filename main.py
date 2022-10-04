# Dict Словари
players = {
    'Carlsen': 2842,
    'Caruana': 2822,
    'Mamedyarov': 2801,
    'Ding': 2797,
    'Giri': 2780
}
# players = dict(Carlsen=2842, Caruana=2822, Mamedyarov=2801, Ding=2797, Giri=2780)
print(players)

top1 = players['Carlsen']
print(top1)
print(players.get('Carlsen'))

players['So'] = 2781
del players['So']

keys = players.keys()
print(type(keys))
print(keys)
# Иногда удобнее работать со списком ключей
keys = list(players.keys())
print(type(keys))
print(keys)
print(sorted(players.keys()))

print('Carlsen' in players)
print('Kramnik' not in players)

vals = players.values()
print(type(vals))
print(vals)
# При создании копии возвращается шеллоу копи(поверхностная копия)
# #внутренняя репрезентация объекта скопирована не будет.
players_copy = players.copy()
print(players_copy)

# синтаксис для пробегания циклом по словарю
for k, v in players.items():
    print(k, v)
items = players.items()
print(type(items))
print(items)

players.pop('Giri')
print(items)
print(players.popitem())
print(players)

print(len(players))

players.setdefault('Karjakin')
print(players)
