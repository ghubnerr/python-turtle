import colorgram
import turtle
from random import randint

NUM_COLORS = 30

# Creating the turtle
kevin = turtle.Turtle()  # Creates a Turtle object instantiation
kevin.shape("turtle")  # Changes the shape of the object
kevin.fillcolor("azure")  # Colors from Tk (tkinter package for GUI) color specification string
turtle.colormode(255)
kevin.hideturtle()

# Extracting colors
image_colors = colorgram.extract('A Starry Night.jpg', NUM_COLORS)
proportions = {}
for color in image_colors:
    r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
    new_color = (r, g, b)
    proportions[color.proportion] = new_color


def generate_color():
    selector = randint(0, NUM_COLORS-1)
    keys = []
    for key in proportions.keys():
        keys.append(key)
    return proportions[keys[selector]]


# Inspired by Damien Hirst's art style -- ARTWORK: Van Gogh's Starry Night
def draw_a_dot(colors, gap, dot_size):
    kevin.forward(gap)
    kevin.dot(dot_size, colors)


def first_dot(colors, dot_size):
    kevin.pencolor(colors)
    kevin.dot(dot_size, colors)


def draw(dot_size=20, gap=50, num_rows=10, dots_per_row=10):
    kevin.speed(100)
    kevin.pensize(20)
    kevin.penup()
    kevin.rt(90)
    kevin.forward((gap * (num_rows - 0.5) / 2))
    kevin.rt(90)
    kevin.forward((gap * (dots_per_row - 0.5) / 2))
    kevin.rt(180)
    row_num = 1
    for _ in range(num_rows):
        first_dot(generate_color(), dot_size)
        for _ in range(dots_per_row):
            draw_a_dot(generate_color(), gap, dot_size)
        if row_num % 2 == 1:
            kevin.rt(-90)
            kevin.forward(gap)
            kevin.rt(-90)
        else:
            kevin.lt(-90)
            kevin.forward(gap)
            kevin.lt(-90)
        row_num += 1

draw(20,50)

screen = turtle.Screen()
screen.exitonclick()