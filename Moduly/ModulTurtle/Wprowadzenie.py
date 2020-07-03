import turtle


def kwadrat(name, length=100, speed=1):
    name.speed(speed)
    for i in range(4):
        name.forward(length)
        name.left(90)


def complicated(name):
    name.speed(1000)
    for i in range(300):
        name.forward(i)
        name.right(88)


def heart(name, color='red', speed=2):
    name.color('white')
    name.sety(-390)
    name.color(color)
    name.speed(speed)
    name.left(45)
    name.forward(500)
    name.speed(speed * 5)
    name.circle(250, 180)
    name.right(90)
    name.circle(250, 180)
    name.speed(speed)
    name.forward(500)


def randomshape(name):
    import random
    name.speed(1000)
    name.pencolor('pink')
    for i in range(300):
        name.forward(100)
        name.right(random.randint(1, 90))


zolwik = turtle.Turtle()

zolwik.pensize(1)

# kwadrat(zolwik)
# complicated(zolwik)
# heart(zolwik)
randomshape(zolwik)

turtle.exitonclick()
