import turtle
import random
from time import sleep


def displacement(turtle_class, x: int, y: int):
    turtle_class.up()
    turtle_class.goto(x, y)
    turtle_class.down()


def draw_triangle(turtle_class, points, color):
    displacement(turtle_class, points[0][0], points[0][1])
    turtle_class.fillcolor(color)
    turtle_class.begin_fill()
    turtle_class.goto(points[1][0], points[1][1])
    turtle_class.goto(points[2][0], points[2][1])
    turtle_class.goto(points[0][0], points[0][1])
    turtle_class.end_fill()


def set_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(turtle_class, points, triangles):
    list_of_colors = ['red', 'violet', 'green', 'blue', 'grey', 'orange', 'yellow', 'pink']
    draw_triangle(turtle_class, points, list_of_colors[random.randint(0, len(list_of_colors)-1)])
    if triangles > 7:
        sleep(0.3)
    if triangles > 0:
        sierpinski(turtle_class, [points[0], set_mid(points[0], points[1]), set_mid(points[0], points[2])], triangles-1)
        sierpinski(turtle_class, [points[1], set_mid(points[0], points[1]), set_mid(points[1], points[2])], triangles-1)
        sierpinski(turtle_class, [points[2], set_mid(points[2], points[1]), set_mid(points[0], points[2])], triangles-1)

amount_of_triangles = input('Podaj ile ma być trójkątów:(Najlepiej podać liczbę z przedziału 2-4)\n')
try:
    amount_of_triangles = int(amount_of_triangles)
except ValueError:
    amount_of_triangles = input('Podaj liczbę jeszcze raz:\n')

zolwik = turtle.Turtle()
zolwik.hideturtle()
zolwik.speed(0)
if 8 > amount_of_triangles >= 5:
    list_of_points = [[-200, -100], [0, 200], [200, -100]]
elif amount_of_triangles >= 8:
    list_of_points = [[-400, -300], [0, 400], [400, -300]]
else:
    list_of_points = [[-100, -50], [0, 100], [100, -50]]
sierpinski(zolwik, list_of_points, amount_of_triangles)

turtle.exitonclick()
