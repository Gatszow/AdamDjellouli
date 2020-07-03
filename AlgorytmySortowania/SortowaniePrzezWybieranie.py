import random


def find_min_index(_list):
    minimum = _list[0]
    min_index = 0
    for iterator in range(1, len(_list)):
        if minimum > _list[iterator]:
            minimum = _list[iterator]
            min_index = iterator
    return min_index


def selection_sort(_list):
    for iterator in range(len(_list)):
        temp = _list[iterator]
        min_index = find_min_index(_list[iterator:len(_list)]) + iterator
        _list[iterator] = _list[min_index]
        _list[min_index] = temp
    return _list


print(find_min_index([5, 2, 3, 1]))

List = [5, 9, 11, 2, 42, 22, 3, 4, 6, 77, 88, 454, 243, 333, 23]

print('Lista przed posortowaniem:\n{}'.format(List))

print('\nLista po posortowaniu:\n{}'.format(selection_sort(List)))

RandomList = []
for i in range(10):
    RandomList.append(random.randint(0, 100))

print('\nRandomowa lista przed posortowaniem:\n{}'.format(RandomList))

print('\nRandomowa lista po posortowaniu:\n{}'.format(selection_sort(RandomList)))
