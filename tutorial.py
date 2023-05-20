from turtle import Turtle, Screen, colormode  # or import turtle
import random as r

# import turtle as t -> module aliasing

# You can find documentation details for this library at: https://docs.python.org/3/library/turtle.html
# Turtle is built-in. For external libraries go to: https://pypi.org/

kevin = Turtle()  # Creates a Turtle object instantiation
kevin.shape("turtle")  # Changes the shape of the object
kevin.fillcolor("azure")  # Colors from Tk (tkinter package for GUI) color specification string
colormode(255)

directions = [0, 90, 180, 270]


# Drawing a dashed line example using for loops:


def dashed_line(strokes, stroke_length, gap=1):
    for _ in range(strokes):
        kevin.forward(stroke_length)
        kevin.penup()
        kevin.forward(gap)
        kevin.pendown()


def pick_random_rgb_color():
    """Returns a tuple of random RGB numbers"""
    red = r.randint(1, 255)  # Picking a base color randomly
    green = r.randint(1, 255)
    blue = r.randint(1, 255)
    return red, green, blue


def polygon(num_sides, side_length):
    """Draws according to the formula   angle = (n-2)*180/n """
    for _ in range(num_sides):
        kevin.forward(side_length)
        angle = (num_sides - 2) * 180 / num_sides
        kevin.rt(180 - angle)


def draw_shapes(lower_bound, upper_bound, side_length):
    """Draws shapes with num_sides from lower_bound to upper_bound, inclusive"""
    for n in range(lower_bound, upper_bound + 1):
        kevin.pencolor(pick_random_rgb_color())
        polygon(n, side_length)


def random_walk(walks, pen_size, step_size):
    """Walks a step_size, changes color and direction randomly"""
    for _ in range(walks):
        kevin.pensize(pen_size)
        kevin.speed(10)
        kevin.setheading(r.choice(directions))
        kevin.pencolor(pick_random_rgb_color())
        kevin.forward(step_size)
    kevin.speed(6)


# Keep it at the bottom of the file so that it runs only after all the code has been executed.
screen = Screen()
screen.exitonclick()
