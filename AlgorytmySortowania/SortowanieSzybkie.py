import random


def speed_sort(user_list: list):
    mniejsze = []
    rowne = []
    wieksze = []

    if len(user_list) > 1:
        piwot = user_list[0]
        for x in user_list:
            if x > piwot:
                wieksze.append(x)
            elif x == piwot:
                rowne.append(x)
            else:
                mniejsze.append(x)
        return speed_sort(mniejsze) + rowne + speed_sort(wieksze)

    else:
        return user_list


def speed_sort_2(userlist: list):
    if len(userlist) > 1:
        return speed_sort_2([x for x in userlist[1:] if x < userlist[0]]) + [x for x in userlist if x == userlist[0]] + speed_sort_2([x for x in userlist[1:] if x > userlist[0]])
    else:
        return userlist

lista = [random.randint(0, 100) for x in range(15)]
print('Losowa lista przed posortowaniem', lista)
print('Losowa lista po posortowaniu', speed_sort(lista))
print('Losowa lista po posortowaniu', speed_sort_2(lista))
