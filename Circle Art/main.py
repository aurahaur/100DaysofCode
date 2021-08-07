import turtle as t
from turtle import Screen as s
import random

# import heroes
# print(heroes.gen())

# Draw a Square - Challenge 1
# timmy_the_turtle = t()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("green")
#
#
# def timmy_right():
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
#
# for i in range(4):
#     timmy_right()

# Draw a Dashed Line - Challenge 2
# def dashed_line():
#     tim.pendown()
#     tim.forward(20)
#     tim.penup()
#     tim.forward(30)
#
#
# tim = t()
# tim.shape("turtle")
# tim.color("black")
# tim.penup()
# tim.back(300)
#
# for i in range(12):
#     dashed_line()

# Draw Different Shapes - Challenge 3
# Triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# import random
#
# colours = ["black", "green", "red", "blue", "magenta", "yellow", "orange", "chocolate",
#            "brown", "coral", "DeepPink"]
#
#
# def draw_shapes(number_of_sides):
#     angle = 360 / number_of_sides
#     for _ in range(number_of_sides):
#         tim.forward(50)
#         tim.right(angle)
#
#
# # def triangle():
# #     tim.forward(50)
# #     tim.right(120)
# #
# #
# # def square():
# #     tim.forward(50)
# #     tim.right(90)
# #
# #
# # def pentagon():
# #     tim.forward(50)
# #     tim.right(72)
# #
# #
# # def hexagon():
# #     tim.forward(50)
# #     tim.right(60)
# #
# #
# # def heptagon():
# #     tim.forward(50)
# #     tim.right(51.42)
# #
# #
# # def octagon():
# #     tim.forward(50)
# #     tim.right(45)
# #
# #
# # def nonagon():
# #     tim.forward(50)
# #     tim.right(40)
# #
# #
# # def decagon():
# #     tim.forward(50)
# #     tim.right(36)
#
#
# tim = t()
# for _ in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shapes(_)
#
# # for _ in range(3):
# #     triangle()
# #
# # tim.color(random.choice(colours))
# # for _ in range(4):
# #     square()
# #
# # tim.color(random.choice(colours))
# # for _ in range(5):
# #     pentagon()
# #
# # tim.color(random.choice(colours))
# # for _ in range(6):
# #     hexagon()
# #
# # tim.color(random.choice(colours))
# # for _ in range(7):
# #     heptagon()
# #
# # tim.color(random.choice(colours))
# # for _ in range(8):
# #     octagon()
# #
# # tim.color(random.choice(colours))
# # for _ in range(9):
# #     nonagon()
# #
# # tim.color(random.choice(colours))
# # for _ in range(10):
# #     decagon()

# Draw a Random Walk - Challenge 4
# import random
#
# direction = [0, 90, 180, 270]
# colours = ["black", "green", "red", "blue", "magenta", "yellow", "orange", "chocolate",
#            "brown", "coral", "DeepPink"]
#
# tim = t()
# tim.pensize(5)
# tim.speed(0)
#
#
# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.setheading(random.choice(direction))
#     tim.forward(20)
# Generate Random Colours - Challenge 5
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     red = random.randint(0, 255)
#     green = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     return (red, green, blue)
#
#
# direction = [0, 90, 180, 270]
#
# tim.pensize(5)
# tim.speed(0)
#
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(20)
# Draw a Spirograph - Challenge 6
tim = t.Turtle()
t.colormode(255)
r = 100
t.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


for _ in range(36):
    t.pencolor(random_color())
    t.circle(r)
    t.setheading(t.heading() + 10)

screen = s()
screen.exitonclick()
