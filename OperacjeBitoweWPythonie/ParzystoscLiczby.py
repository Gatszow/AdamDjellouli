

def research_parity(number: int):
    if number & 1 == 0:
        return 'Liczba {} jest parzysta.'.format(number)
    return 'Liczba {} nie jest parzysta.'.format(number)


numbers = [research_parity(x) for x in range(1, 11)]
for i in numbers:
    print(i)
