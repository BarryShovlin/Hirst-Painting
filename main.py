# import colorgram
import turtle
import random
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
"""uses colorgram to extract rgb values of colors in the image."""
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     shade = (r, g, b)
#     rgb_colors.append(shade)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163,
              184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160,
              142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147,
              17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t = turtle.Turtle()
t.shape("turtle")
screen = turtle.Screen()
turtle.colormode(255)
pos = t.pos()
t.hideturtle()
t.speed("fastest")


def draw_dot():
    t.dot(20, color_list[random.randint(0, len(color_list) - 1)])
    t.penup()
    t.forward(50)


def line():
    for _ in range(10):
        draw_dot()
    t.left(180)
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)


def draw_picture():
    for _ in range(10):
        line()


t.setheading(225)
t.penup()
t.forward(400)
t.setheading(0)
draw_picture()
screen.exitonclick()
