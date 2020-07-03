
vowels = 'aeiouy'


def count_consonants_iteration(string: str):
    result = 0
    for x in string:
        if x.isalpha() and x.lower() not in vowels:
            result += 1
    return result


def count_consonants_recursion(string: str):
    if len(string) == 0:
        return 0
    if string[0].isalpha() and string[0].lower() not in vowels:
        return 1 + count_consonants_recursion(string[1:])
    return count_consonants_recursion(string[1:])


List = ['tunczyk', 'Brokuly', 'James', 'Kapitan']

for word in List:
    print('W słowie {} jest {} spolglosek'.format(word, count_consonants_iteration(word)))
    print('W słowie {} jest {} spolglosek'.format(word, count_consonants_recursion(word)))
