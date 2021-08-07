from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 circle
        self.color("red")
        self.speed("fastest")
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        self.goto(rand_x, rand_y)
        self.refresh_location()

    def refresh_location(self):
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        self.goto(rand_x, rand_y)
