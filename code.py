from turtle import *

# Setup speed and background color
speed(0)
bgcolor('black')

# Function to draw a petal
def draw_petal(radius, color, angle=60):
    pencolor('black')  # Outline color
    fillcolor(color)
    begin_fill()
    circle(radius, angle)  # Draw arc for half petal
    lt(120)
    circle(radius, angle)
    lt(120)
    end_fill()

# Function to draw a full flower with n petals
def draw_flower(petal_count, petal_radius, petal_color):
    for _ in range(petal_count):
        draw_petal(petal_radius, petal_color)  # Draw one petal
        rt(360 / petal_count)  # Rotate to position the next petal

# Draw concentric circles with a floral touch
def draw_concentric_flower():
    up()
    goto(0, -150)
    down()

    # First circle with orange petals
    pen(fillcolor="orange", pencolor="magenta", pensize=2)
    begin_fill()
    circle(150)  # Outer circle
    end_fill()

    # First set of petals
    up()
    goto(0, -120)
    down()
    draw_flower(12, 100, 'red')  # Red petals around the first circle

    # Second circle with purple
    up()
    goto(0, -90)
    down()
    pen(fillcolor="purple", pencolor="white", pensize=2)
    begin_fill()
    circle(90)  # Middle circle
    end_fill()

    # Second set of petals (pink)
    up()
    goto(0, -70)
    down()
    draw_flower(10, 70, 'pink')  # Pink petals around the second circle

    # Third circle with magenta
    up()
    goto(0, -50)
    down()
    pen(fillcolor="magenta", pencolor="white", pensize=2)
    begin_fill()
    circle(50)  # Inner circle
    end_fill()

    # Third set of petals (white)
    up()
    goto(0, -40)
    down()
    draw_flower(8, 40, 'white')  # White petals around the third circle

# Central soft flower
def draw_center_flower():
    up()
    goto(0, 0)
    down()
    draw_flower(6, 30, 'purple')  # Soft central purple flower

# Call the functions to draw the full pattern
draw_concentric_flower()  # Draw the concentric flower patterns
draw_center_flower()  # Draw the central soft flower

# Hide the turtle and complete
ht()
exitonclick()
