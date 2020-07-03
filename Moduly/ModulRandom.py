import random

colors = ['czarny', 'zielony', 'niebieski', 'pomarańczowy', 'różowy']

random_choices = random.choices(colors, weights=[50, 30, 30, 10, 5], k=20)
print(random_choices)


anotherlist = random.sample(list(range(0, 30)), k=10)
print(anotherlist)


random.shuffle(anotherlist)
print(anotherlist)

# random.normalvariate(mean [średnia], standard deviation [odchylenie standardowe])
print(random.normalvariate(3, 0.2))
