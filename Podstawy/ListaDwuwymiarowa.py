import random


def print_2d(_list):
    for iterator in range(len(_list)):
        for j_terator in range(len(_list)):
            print(_list[iterator][j_terator], end=' ')
        print('')


list2D = [[1, 2, 3, 4],
          [1, 5, 7],
          [2, 9, 100]]

print_2d(list2D)
print('')

list2D[1][2] = 'tunczyk'
print_2d(list2D)

print('')

list1D = []
list2D.clear()

for j in range(10):
    for i in range(10):
        list1D.append(random.randint(0, 100))
    list2D.append(list1D)
    list1D = []

print_2d(list2D)
print('')

tabliczka = []
rzad = []

for i in range(1, 11):
    for j in range(1, 11):
        rzad.append(i * j)
    tabliczka.append(rzad)
    rzad = []

print_2d(tabliczka)
