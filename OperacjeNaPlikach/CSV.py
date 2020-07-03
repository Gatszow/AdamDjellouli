import csv

with open('Zeszyt.csv') as csv_file:
    readerCSV = csv.reader(csv_file, delimiter=';')

    # Wczytujemy naglowki
    headings = next(readerCSV)

    # wczytujemy wiersze
    rows = [row for row in readerCSV]

    print(headings)
    print(rows[0])


    # liczymy srednia
    Sum = 0
    for row in rows:
        Sum += float(row[2])
    mean = Sum/len(rows)
    print('%.2f' % mean)

with open('Zeszyt2.csv', mode='w') as csv_file:
    headings = ['pracownik', 'stanowisko', 'pensja']
    List = [{'pracownik':'Jan', 'stanowisko':'Biegacz', 'pensja':'1000'},
            {'pracownik':'Brokul', 'stanowisko':'Dietetyk', 'pensja':'3000'},
            {'pracownik':'James', 'stanowisko':'Dyrektor', 'pensja':'20'}]
    writer = csv.DictWriter(csv_file, fieldnames=headings)
    writer.writeheader()
    for x in List:
        writer.writerow(x)

with open('Zeszyt2.csv') as csv_file:
    readerCSV = csv.reader(csv_file, delimiter=';')
    rows = [wiersz for wiersz in readerCSV if wiersz]
    for row in readerCSV:
        print(row)
