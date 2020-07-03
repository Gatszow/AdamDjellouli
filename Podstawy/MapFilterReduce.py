from functools import reduce

# map dwa argumenty:
# pierwszy: inna funkcja
# drugi: struktura
# zwraca zmodyfikowana strukture


def kwadrat(lista: list):
    lista2 = [lista[i]**2 for i in range(len(lista))]
    return lista2


def kwadracik(liczba: int):
    return liczba**2


Lista = [2, 5, 6, 8, 4]
print(Lista)
print(kwadrat(Lista))
print(list(map(kwadracik, Lista)))


# filter dwa argumenty:
# pierwszy: inna funkcja (zawiera warunek)
# drugi: struktura
# zwraca odfiltrowana strukture


def wieksze5(lista: list):
    lista2 = [lista[i] for i in range(len(lista)) if lista[i] > 5]
    return lista2


def filtr5(x):
    if x > 5:
        return x


print(wieksze5(Lista))
print(list(filter(filtr5, Lista)))

# reduce dwa argumenty:
# pierwszy: funkcja, która zwraca jakis wynik i przyjmuje 2 argumenty
# drugi: struktura
# zwraca wynik


def suma(lista: list):
    suma = 0
    for x in lista:
        suma += x
    return suma


def dodaj(a, b):
    return a + b


print(suma(Lista))
print(reduce(dodaj, Lista))
