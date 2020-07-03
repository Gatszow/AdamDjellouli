# -*- coding: utf-8 -*-
import funkcje
from time import sleep

inputlist = []

print("Witaj w programie wyszukującym podaną liczbę lub słowo w liście!!")

# tryb = int(input("Najpierw proste pytanie:\nChcesz wyszukać słowo [1] czy liczbę [2]?\n"))
templist = input("Podaj elementy, które znajdują się na liście (oddzielone przecinkiem):\n")

templist = templist.split(",")
print(templist)
print("Tworzenie listy...")
sleep(5)

for word in templist:
    word = word.strip()
    inputlist.append(word)
print(inputlist)
word = input("Podaj element, który chcesz odszukać\n")

if funkcje.check(inputlist, int):
    print("Wynik:", funkcje.binary_search(inputlist, word, True))

else:
    print("Wynik:", funkcje.linear_search(inputlist, word, True))
