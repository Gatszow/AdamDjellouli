import random


def test_pierwszosci(number: int):
    if number <= 1:
        return False
    for iterator in range(2, int(number**0.5)):
        if number % iterator == 0:
            return False
    return True


liczba1 = random.randint(2, 1000000)
liczba2 = random.randint(2, 1000000)
liczba3 = random.randint(2, 1000000)

print('Czy liczba {} jest liczbą, pierwszą? {}'.format(liczba1, test_pierwszosci(liczba1)))
print('Czy liczba {} jest liczbą, pierwszą? {}'.format(liczba2, test_pierwszosci(liczba2)))
print('Czy liczba {} jest liczbą, pierwszą? {}'.format(liczba3, test_pierwszosci(liczba3)))

i = 0
while not test_pierwszosci(liczba1):
    liczba1 = random.randint(2, 1000000)
    i += 1

print('liczba ', liczba1)
print(i)
