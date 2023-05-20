from turtle import Turtle, Screen, colormode
import random as r

kevin = Turtle()
kevin.shape("turtle")
kevin.fillcolor("azure")
colormode(255)


def pick_random_rgb_color():
    """Returns a tuple of random RGB numbers"""
    red = r.randint(1, 255)  # Picking a base color randomly
    green = r.randint(1, 255)
    blue = r.randint(1, 255)
    return red, green, blue


def spirograph(num_circles, circle_size):
    kevin.speed(100)
    for _ in range(num_circles):
        kevin.pencolor(pick_random_rgb_color())
        kevin.rt(360 / num_circles)
        kevin.circle(circle_size)


spirograph(90,100)

screen = Screen()
screen.exitonclick()
