import datetime
import os

# nazwa systemu
print(os.name)

# folder w którym aktualnie jestesmy
print(os.getcwd())

# sciezka absolutna
print(os.path.abspath('..'))

# wyswietlenie zawartosci folderu w ktorym jestesmy
print(os.listdir('..'))

# przechodzenie miedzy folderami
# os.chdir(sciezka)

# tworzenie nowego folderu
# os.mkdir('folder')

# usuwanie folderu
os.rmdir('folder')

# tworzymy plik
with open('ModulOS.txt', mode='w') as file:
    pass

# zmiana nazwy
os.rename('ModulOS.txt', 'ModulOS2.txt')

# info o pliku
print(os.stat('ModulOS2.txt'))

# czas ostatniej modyfikacj
print(datetime.datetime.fromtimestamp(os.stat('ModulOS2.txt').st_mtime))

# usuwamy plik
os.remove('ModulOS2.txt')

# walk przechodzi przez wszystkie foldery znajdujace sie w obecnym folderze
# zwraca informacje o sciezce, o folderach i plikach

folder = os.getcwd()
for path, folders, files in os.walk(folder):
    print('\nSciezka: {}\nFoldery: {}\nPliki: {}'.format(path, folders, files))
