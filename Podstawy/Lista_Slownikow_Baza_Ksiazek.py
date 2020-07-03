from operator import itemgetter


def add_book(listofbooks, keys):
    # lista przechowujaca wartosci dla pojedynczego slownika
    list_ = []
    while 1:
        title_ = input('Podaj tytul ksiazki:\n')
        if if_book(listofbooks, title_):
            print('Ksiazka o tytuke {} jest już w bazie'.format(title_))
        else:
            list_.append(title_)
            break
    author = input('Podaj autora ksiazki:\n')
    list_.append(author)
    publication_date = int(input('Podaj rok wydania ksiazki:\n'))
    list_.append(publication_date)
    price = int(input('Podaj cene ksiazki:\n'))
    list_.append(price)
    number_of_pages = int(input('Podaj liczbe stron ksiazki:\n'))
    list_.append(number_of_pages)

    # dodajemy ksiazke do listy ksiazek
    listofbooks.append(dict(zip(keys, list_)))


def del_book(listofbooks, title_):
    for book in listofbooks:
        if title_ == book['Tytul']:
            del book
            break


def the_cheapest_book(listofbooks):
    cheapest = list_of_books[0]['Cena']
    index = 0
    for iterator in range(1, len(listofbooks)):
        if list_of_books[iterator]['Cena'] < cheapest:
            cheapest = list_of_books[iterator]['Cena']
            index = iterator
    return index


def the_most_expensive_book(listofbooks):
    most_expensive = listofbooks[0]['Cena']
    index = 0
    for iterator in range(1, len(listofbooks)):
        if most_expensive < listofbooks[iterator]['Cena']:
            most_expensive = listofbooks[iterator]['Cena']
            index = iterator
    return index


def show(listofbooks, keys):
    iteration = 1
    for book in listofbooks:
        print('Ksiazka numer ', iteration)
        print(' '.join(str(book[key]) for key in keys))
        print(' ')
        iteration += 1


def if_book(listofbooks, title_):
    for book in listofbooks:
        if title_ == book['Tytul']:
            return True
    return False


# lista slownikow, reprezentuje ksiazki w ksiegarni
list_of_books = []
_keys = ['Tytul', 'Autor', 'Rok wydania', 'Cena', 'Liczba stron']

for i in range(3):
    print("Książka nr", i+1)
    add_book(list_of_books, _keys)

show(list_of_books, _keys)

print('Lista posortowana wedlug ceny')
show(sorted(list_of_books, key=itemgetter('Cena')), _keys)
print('Lista posortowana odwrotnie')
show(sorted(list_of_books, key=itemgetter('Cena'), reverse=True), _keys)

print('Najtansza ksiazka:\n{}'.format(list_of_books[the_cheapest_book(list_of_books)]))

while 1:
    show(list_of_books, _keys)
    title = input('Podaj nazwe ksiazki do usuniecia\n')
    if not if_book(list_of_books, title):
        print('Ksiazka o tytule {} jest juz w bazie'.format(title))
    else:
        del_book(list_of_books, title)
        print('Poprawnie usunieto')
        break

show(list_of_books, _keys)
