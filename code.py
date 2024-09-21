from turtle import *

speed(0)
bgcolor('black')

def draw_petal(radius, color, angle=60):
    pencolor('black')
    fillcolor(color)
    begin_fill()
    circle(radius, angle)
    lt(120)
    circle(radius, angle)
    lt(120)
    end_fill()

def draw_flower(petal_count, petal_radius, petal_color):
    for _ in range(petal_count):
        draw_petal(petal_radius, petal_color)
        rt(360 / petal_count)

def draw_concentric_flower():
    up()
    goto(0, -150)
    down()

    pen(fillcolor="orange", pencolor="magenta", pensize=2)
    begin_fill()
    circle(150)
    end_fill()

    up()
    goto(0, -120)
    down()
    draw_flower(12, 100, 'red')

    up()
    goto(0, -90)
    down()
    pen(fillcolor="purple", pencolor="white", pensize=2)
    begin_fill()
    circle(90)
    end_fill()

    up()
    goto(0, -70)
    down()
    draw_flower(10, 70, 'pink')

    up()
    goto(0, -50)
    down()
    pen(fillcolor="magenta", pencolor="white", pensize=2)
    begin_fill()
    circle(50)
    end_fill()

    up()
    goto(0, -40)
    down()
    draw_flower(8, 40, 'white')

def draw_center_flower():
    up()
    goto(0, 0)
    down()
    draw_flower(6, 30, 'purple')

draw_concentric_flower()
draw_center_flower()

ht()
exitonclick()
