# znajdujemy liczby pierwsze z przedziału podanego przez użytkownika
# we find primes from from user input range


def sieve_of_Eratosthenes(start: int, end: int):
    temp = [1 for x in range(end+1)]
    for i in range(2, end+1):
        for j in range(i + 1, end+1):
            if j % i == 0:
                temp[j] = 0
    primes = []
    for i in range(start, len(temp)):
        if temp[i] == 1:
            primes.append(i)
    return primes


def sieve_of_Eratosthenes_2(start: int, end: int):
    primes = []
    temp = [True]*(end+1)
    for i in range(2, end):
        if temp[i]:
            if i >= start:
                primes.append(i)
            for j in range(i * i, end + 1, i):
                temp[j] = False
    return primes


print("Jest to program wypisujący liczby pierwsze\n{}".format("*"*80), end="")

start_of_range = input("Podaj początek przedziału liczb:\n")
while True:
    try:
        start_of_range = int(start_of_range)
        if start_of_range <= 2:
            raise ValueError
        break
    except ValueError:
        start_of_range = input("Wprowadzono niepoprawny typ danych, musi zostać wprowadzona "
                               "liczba, należąca do przedziału {2, 3, 4, 5, 6...}\n"
                               "Wprowadź początek przedziału raz jeszcze:\n")


print("*"*80, end="")

end_of_range = input("Podaj koniec przedziału liczb:\n")
while True:
    try:
        end_of_range = int(end_of_range)
        if end_of_range <= start_of_range:
            raise ValueError
        break
    except ValueError:
        end_of_range = input("Wprowadzono niepoprawny typ danych, musi zostaać wprowadzona liczba całkowita, "
                             "większa od liczby wprowadzonej jako początek przedziału\n"
                             "Wprowadź koniec przedziału raz jeszcze:\n")


print("*"*80, end="")
print("Liczby pierwsze z podanego przedziału, to:")

# print(sieve_of_Eratosthenes(start_of_range, end_of_range))

print(sieve_of_Eratosthenes_2(start_of_range, end_of_range))
