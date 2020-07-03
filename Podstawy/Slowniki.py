import random


def add_name(dictonary: dict, list_of_names: list):
    for name in list_of_names:
        if name not in dictonary:
            dictonary[name] = 1
        else:
            dictonary[name] = dictonary[name] + 1


def how_many(dictonary: dict, name: str):
    if name in dictonary:
        number = dictonary[name]
    else:
        number = 0
    return number


def show_dict(dictonary: dict):
    for key in dictonary:
        if dictonary[key] == 1:
            print('Element o nazwie', key, 'wystapil', dictonary[key], 'raz')
        else:
            print('Element o nazwie', key, 'wystapil', dictonary[key], 'razy')


ditry = dict()

names = ['Tunczyk', 'James', 'Jerzy', 'Adam', 'Adam',
         'Adam', 'Tunczyk', 'Brokul', 'Adam', 'Tunczyk']

add_name(ditry, names)
print('\nCały slownik\n{}'.format(ditry))

print('\nFunkcja wyswietlajaca caly slownik, jedno imie pod drugim wraz z iloscia wystapienia:')
show_dict(ditry)

print('\nIle razy jest w slowniku interesujace nas imie (w tym przypadku Adam):')
print(how_many(ditry, 'Adam'), 'razy')

print("\nTeraz wprowadźmy losowość")

new_list = []
new_dict = {}

for x in range(50):
    for i in range(100):
        new_list.append(names[random.randint(0, len(names)-1)])
    add_name(new_dict, new_list)
    new_list = []

show_dict(new_dict)
