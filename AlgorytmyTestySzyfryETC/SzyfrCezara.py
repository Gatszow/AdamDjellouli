# -*- coding: utf-8 -*-
from time import sleep


def caesar_cipher(message: str, key: int, deciphering=False):
    """Funkcja realizująca algorytm szyfru Cezar"""

    # zmienna przechowująca zaszyfrowaną wiadomość
    encoded_message = ''

    for x in message:

        # sprawdzenie czy x to litera
        if x.isalpha():

            # zamiana znaku na reprezentacje liczbową
            number = ord(x)

            # przesunięcie reprezentacji liczbowej znaku o klucz pozycji
            if deciphering:
                number -= key
            else:
                number += key

            # sprawdzenie wielkości litery
            if x.isupper():
                if deciphering:
                    if number < 65:
                        number += 26
                else:
                    if number > 90:
                        number -= 26

            else:
                if deciphering:
                    if number < 97:
                        number += 26
                else:
                    if number > 122:
                        number -= 26
            # powrót do reprezentacji znakowej oraz budowa zaszyfrowanej wiadomości
            encoded_message += chr(number)
        else:
            encoded_message += x

    return encoded_message


# zmienna zapewniająca działanie programu
programisworking = True


# Główny kod
while programisworking:
    mysterious_tip = int(input("Wybierz 1, gdy chcesz przejść do podpowiedzi co do klucza"
                               "\nWybierz 2, jak chcesz przejść wprost do programu\nTwój wybór: "))

    if mysterious_tip == 1:
        print("Wskazówka brzmi tak:"
              "\nJest to liczba jednocześnie istotna, jak i nieistotna"
              "\nJest to liczba nieduża, lecz wielka dla nas"
              "\nLiczba ta się nie zmienia, a jednak chcemy, żeby było jej jak najwięcej"
              "\nŻycie bez tej liczby przemijałoby wolniej"
              "\nLiczby, wszędzie liczby, a cóż to za liczba, czy wiesz?")

    elif mysterious_tip == 2:
        print("Program się uruchamia")
        sleep(5)

    else:
        print("Wskazówka pominięta, zła liczba wciśnięta")

    # szyfrowanie czy odszyfrowanie
    choice = int(input("Wybierz tryb:\n1. Szyfrowanie\n2. Odszyfrowanie\nWybieram tryb (1/2):\n")) - 1

    # wiadomość do szyfrowania/odszyfrowania
    user_message = input("Podaj swoją wiadomość:\n")

    # klucz szyfru oraz sprawdzenie, czy klucz jest prawidłowy
    user_key = int(input("Podaj swój klucz:\n"))

    while True:
        if user_key < 1:
            user_key = int(input("Niewłaściwy klucz, podaj liczbę naturalną dodatnią, większą niż 1:\n"))
            continue
        break

    print("Twoja zaszyfrowana wiadomość to:\n{}".format(caesar_cipher(user_message, user_key, bool(choice))))

    programisworking_choice = input("Czy zakończyć dzialanie programu? T/N ").upper()

    if programisworking_choice == "T":
        programisworking = False
    else:
        print("Program działa dalej!!")
