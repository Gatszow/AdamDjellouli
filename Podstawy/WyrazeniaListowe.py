# sposob 'na piechote'

List = []
for x in range(10):
    List.append(x+1)
print(List)


# wyrazenia listowe

# List = [wyrazenie for element in zbior if warunek]
List = [x+1 for x in range(10)]
print(List)

# 1^3, 2^3, 3^3, 4^3, 5^3 ... 10^3
List = [(x+1)*(x+1)*(x+1) for x in range(10)]
print(List)

# 2^3, 4^3, 6^3, 8^3, 10^3
List = [(x+1)*(x+1)*(x+1) for x in range(10) if (x+1) % 2 == 0]
print(List)

# 30, 60, 90
List = [x for x in range(1, 100) if x % 2 == 0 and x % 3 == 0 and x % 5 == 0]
print(List)

#
shopping = ['tunczyk', 'brokul', 'groszek', 'fasolka', 'kukurydza', 'grahamki']

# brokul
for purchase in shopping:
    if purchase.startswith('b'):
        print(purchase)

# ['brokul']
bshopping = [purchase for purchase in shopping if purchase.startswith('b')]
print(bshopping)

# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2] ... [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
List2D = [[i+1]*10 for i in range(10)]
print(List2D)