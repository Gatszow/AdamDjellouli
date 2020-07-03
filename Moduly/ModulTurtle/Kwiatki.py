import turtle


def draw_arch(turtle_class, length):
    n = int(length/2)
    for i in range(n):
        turtle_class.forward(length/n)
        turtle_class.left(60/n)


def draw_petal(turtle_class, length):
    draw_arch(turtle_class, length)
    turtle_class.left(120)
    draw_arch(turtle_class, length)


def draw_flower(turtle_class, length, numberofpetals):
    for i in range(1, numberofpetals+1):
        draw_petal(turtle_class, length)
        if number == 4:
            turtle_class.left(35)
        else:
            if i % 3 != 0:
                turtle_class.left(10)
            else:
                turtle_class.left(45)


number = int(input('Podaj numerek\nPS: Najlepiej parzysty oraz większy, niż 2\n'))

zolwik = turtle.Turtle()
zolwik.speed(2)
draw_flower(zolwik, 100, number)

turtle.exitonclick()
