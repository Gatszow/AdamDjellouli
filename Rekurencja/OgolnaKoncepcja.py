# def function():
#     function()


def sum_loop(_list: list):
    Sum = 0
    for x in _list:
        Sum += x
    return Sum


# kazda funkcja rekurencyjna ma dwa przypadki: podstawowy i rekurencyjny


def sum_recursion(_list: list):
    # przypadek podstawowy
    if not _list:
        return 0
    # przypadek rekurencyjny
    else:
        return _list[0] + sum_recursion(_list[1:])


List = [3, 2, 4, 9]
print('Suma poprzez petle:\n{}'.format(sum_loop(List)))
print('\nSuma poprzez rekurencje:\n{}'.format(sum_recursion(List)))

# silnia n = n*(n-1)*(n-2)...
# silnia 3 = 3*2*1 = 6


def factorial_loop(number: int):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial


def factorial_recursion(number: int):
    # przypadek podstawowy
    if number <= 1:
        return 1
    else:
        return number*factorial_recursion(number-1)


print('\nSilnia poprzez petle:\n{}'.format(factorial_loop(3)))
print('\nSilnia poprzez rekurencje:\n{}'.format(factorial_recursion(3)))

# Ciag Fibonacciego
# Pierwszy wyraz ciagu rowny 0, drugi rowny 1, a kazdy nastepny suma dwoch poprzednich


def fibonacci_loop(number: int):
    before_before_sought_number = 0
    before_sought_number = 0
    sought_number = 1
    for i in range(1, number):
        before_before_sought_number = before_sought_number
        before_sought_number = sought_number
        sought_number = before_before_sought_number + before_sought_number
    return sought_number


def fibonacci_recursion(number: int):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)

# Rekurencja dłużej 'mieli'
print('\nCiag Fibonacciego poprzez petle:\n{}'.format(fibonacci_loop(30)))
print('\nCiag Fibonacciego poprzez rekurencje:\n{}'.format(fibonacci_recursion(30)))
