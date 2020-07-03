from random import choice
from time import sleep

print('*'*80, end="")
print('* '*17, '\"Wisielec\"', ' *'*17, end="")
print('*' * 80, end="")

nickname = input("Podaj swój nick: ")
print("\nWitaj {}".format(nickname))

listofpasswords = ['Olga', 'Jasionowska', 'Rafał', 'Kochana', 'Dziewczynka', 'Miła', 'Opiekuńcza', 'Zabawna', 'Piękna',
                   'Inteligentna', 'Jedyna', 'Wymarzona', 'Powalająca']
password = choice(listofpasswords)
table = list(password)
for i in range(len(password)):
    table[i] = '_'


lives = 3
while lives > 0:
    print('\nPozostałe życia:', lives, end='\n\n')
    sleep(1)
    print("Oto hasło do zgadnięcia:\n", ' '.join(table), end="\n\n")

    char = str(input("Podaj swoją literę: "))

    if char in password:
        for i in range(len(password)):
            if password[i] == char:
                table[i] = char
        print('$' * 80, end="")
        print("Udało ci się odgadnąć literkę!!!")
        print('$' * 80, end="")
        sleep(3)

        if ''.join(map(str, table)) == password:
            print(' '.join(table), end="\n\n")
            print('♥' * 80, end="")
            sleep(3)
            print("{}... WYGRANA!!!!".format(nickname))
            sleep(10)
            print('♥' * 80, end="")
            break

    else:
        print(":{" * 39, end="")
        print(" Nieprawidłowa literka ")
        print(":{" * 39, end="")
        sleep(3)
        lives -= 1
        if lives == 0:
            print("Przegrana")
            sleep(10)
