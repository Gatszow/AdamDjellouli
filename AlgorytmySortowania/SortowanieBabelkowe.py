

def babelkowe_sortowanie(userlist: list):
    for i in range(len(userlist)):
        for j in range(len(userlist)-1-i):
             if userlist[j] > userlist[j+1]:
                swap(userlist, j, j+1)
        print("Posortowane po raz", i+1)
        print_list(userlist)


def swap(userlist: list, i, j):
    userlist[i], userlist[j] = userlist[j], userlist[i]
    return userlist


def print_list(userlist: list):
    for x in userlist:
        if x < max(userlist):
            print(x, end=', ')
        else:
            print(x)


lista = [9, 2, 3, 45, 63, 43, 33, 42, 3, 2, 1]

babelkowe_sortowanie(lista)
