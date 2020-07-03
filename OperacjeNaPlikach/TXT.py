rows = []

with open('plik.txt', 'r') as file:
    # print('Liczba wierszy:', len(file.readlines()))
    print(file.name)
    print(file.mode)
    # print(file.readlines())

    for row in file:
        rows.append(file.readline().split())

    numberofwords = 0
    for row in rows:
        numberofwords += len(row)
    print('Liczba slow:', numberofwords)

    '''size = 20
    content = file.read(size)
    while len(content) > 0:
        print(content, end='*')
        content = file.read(size)'''


List = ['czesc', 'test', 'lol', 'tunczyk']

with open('test.txt', 'w') as file:
    for string in List:
        print(string, file=file)


with open('test.txt', 'a') as file:
    # file.write('\ndopisane')
    print('dopisane', file=file)
