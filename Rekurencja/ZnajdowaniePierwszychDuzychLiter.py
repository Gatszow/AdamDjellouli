

def find_big_letter_iteration(word: str):
    for x in word:
        if x.isupper():
            return x
    return -1


def find_big_letter_recursion(word: str):
    if len(word) == 0:
        return -1
    if word[0].isupper():
        return word[0]
    else:
        return find_big_letter_recursion(word[1:])


List = ['Marcepan', 'tunCzyk', 'grzegoRz', 'napis']

for Word in List:
    print(find_big_letter_recursion(Word))
    print(find_big_letter_iteration(Word))
