# 8.1
"""def display_message():
    print('Аргументы и функции')


display_message()
# 8.2


def favorite_book(title):
    print(f'\n One of my favorite books is {title}')


favorite_book('Alice in Wonderland')
# 8.3


def make_tshirt(size, text):
    print(f'Размер футболки {size} с надписью {text}')


make_tshirt('L', 'I love Python')
make_tshirt(size='XL', text='I love Python !')
# 8.4


def make_tshirt(text='I love Python', size='L'):
    print(f'Размер футболки {size} с надписью {text}')


make_tshirt()
make_tshirt('I lern Python')
# 8.5


def describe_city(city, country='Russia'):
    print(f'{city} is in {country}')


describe_city('Moscow')
describe_city('Penza')
describe_city('Pekin', 'China')
# 8.6


def city_country(city, country):
    return print(f'{city}, {country}')


city_country('Moscow', 'Russia')
city_country('Pekin', 'China')
city_country('Buenos Ayres', 'Argentina')
# 8.7
'''def make_album(artist, album, track=''):
    insert_album = [artist, album, track]
    return insert_album'''


def make_album(artist, album, track=''):
    if track:
        insert_album = [artist, album, track]
    else:
        insert_album = [artist, album]
    return insert_album


print(make_album('Elvis', 'Big'))
print(make_album('Elvis', 'Big', '11'))
print(type(make_album))
while True:
    name_artist = input('Enter the name artist or enter "q" to quit:')
    if name_artist == 'q':
        break
    name_album = input('Enter the name album:')
    # tracks = input('Enter the count track:')

    album_list = make_album(name_artist, name_album)
    print(album_list)"""
# 8.9


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['Kolya', 'Vitya', 'Misha']
show_magicians(magicians)
print(type(magicians))
# 8.10


def make_great(magicians):
    for i in magicians:
        magicians = ['Great ' + i]
#        magicians.append(['Great ' + i])
        print(magicians)
    return magicians


# 8.11

copy_magicians = make_great(magicians[:])
print(copy_magicians)
print(type(copy_magicians))
show_magicians(magicians)
show_magicians(copy_magicians)
