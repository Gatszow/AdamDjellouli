zbior = set()

dir(zbior)

print(zbior)

zbior.add(8)
print(zbior)

zbior.add(12)
print(zbior)

zbior.add(100)
print(zbior)

zbior.add('Tunczyk')
print(zbior)

zbior.add(False)
print(zbior)

zbior.add(8.971)
print(zbior)

zbior.add(100)
print(zbior)
print("%%% Jak widac, zbiory nie sa uporzadkowane %%%", end='\n\n')

print('*'*80)

print('\nMozemy wydac pojedyncze elementy zbioru za pomoca petli for:')
for element in zbior:
    print(element)

print('*'*80)

print('\nZa pomoca funkcji len() mozna sprawdzic liczbe elementow w zbiorze')
print(len(zbior))

print('*'*80)

print('\nMozemy usunac elementy zbioru za pomoca discard() i remove():')
zbior.remove(8)
print(zbior)
print(len(zbior))

zbior.discard('Tunczyk')
print(zbior)
print(len(zbior))
print('Roznica miedzy discard() a remove() jest taka, ze jak nie ma elementu w secie,'
      ' a chcemy go usunac, to remove() pokaze error, a discard() nie')

# Jaka różnica między discard a remove?

'''
# Error
zbior.remove(121)


# Brak Erroru
zbior.discard(121)
'''


print('\n{}'.format('*'*80))


koledzy = {'karol', 'james', 'lukas', 'johanes', 'tunczyk'}
przyjaciele = {'brokul', 'banan', 'grzegorz', 'johanes', 'james'}


print('\nSuma setow:')

suma_pierwszy_sposob = koledzy.union(przyjaciele)
print('\nPierwszy sposob:\n', suma_pierwszy_sposob)

suma_drugi_sposob = koledzy | przyjaciele
print('\nDrugi sposob:\n', suma_drugi_sposob)


print('\n{}'.format('*'*80))

print("\nIloczyn setow:")

iloczyn_pierwszy_sposob = koledzy.intersection(przyjaciele)
print('\nPierwszy sposob:\n', iloczyn_pierwszy_sposob)

iloczyn_drugi_sposob = koledzy & przyjaciele
print('\nDrugi sposob:\n', iloczyn_drugi_sposob)

print('\n{}'.format('*'*80))

print('\nRoznica setow:')

roznica_pierwszy_sposob_koledzy = koledzy - przyjaciele
print('\nPierwszy sposob (koledzy):\n', roznica_pierwszy_sposob_koledzy)

roznica_drugi_sposob_koledzy = koledzy.difference(przyjaciele)
print('\nDrugi sposob (koledzy):\n', roznica_drugi_sposob_koledzy)

roznica_pierwszy_sposob_przyjaciele = przyjaciele - koledzy
print('\nPierwszy sposob (przyjaciele):\n', roznica_pierwszy_sposob_przyjaciele)

roznica_drugi_sposob_przyjaciele = przyjaciele.difference(koledzy)
print('\nDrugi sposob (przyjaciele):\n', roznica_drugi_sposob_przyjaciele)
