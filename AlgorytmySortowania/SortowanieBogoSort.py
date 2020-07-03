import random


def bogo_sort(_list: list):
    counter = 0
    while not if_sorted(_list):
        random.shuffle(_list)
        counter += 1
    print('Sortowanie odbylo sie', counter, 'razy')


def if_sorted(_list: list):
    for i in range(1, len(_list)):
        if _list[i] < _list[i - 1]:
            return False
    return True


lista = [random.randint(0, 100) for x in range(5)]
print('Przed posortowaniem:\n{}'.format(lista))

bogo_sort(lista)
print('Po sortowaniu:\n{}'.format(lista))
