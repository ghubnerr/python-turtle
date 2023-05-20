from turtle import Turtle, Screen

kevin = Turtle()
kevin.shape("turtle")
kevin.fillcolor("azure")


def print_google_logo(radius):
    kevin.pensize(radius / 2.5)
    kevin.penup()
    kevin.forward(radius * 1 / 10)
    kevin.pendown()
    kevin.pencolor("blue")
    kevin.forward(radius * 4 / 5 - radius * 1 / 10)
    kevin.rt(270)
    kevin.circle(radius * 8 / 7, -15)
    kevin.circle(radius, -15)
    kevin.pencolor("green")
    kevin.circle(radius * 5 / 6, -140)
    kevin.pencolor("yellow")
    kevin.circle(radius * 8 / 7, -35)
    kevin.pencolor("red")
    kevin.circle(radius * 5 / 6, -105)
    kevin.penup()
    kevin.rt(130)
    kevin.forward(100)


print_google_logo(100)


screen = Screen()
screen.exitonclick()