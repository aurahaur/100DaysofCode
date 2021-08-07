from turtle import Turtle
import random


class Star:

    def __init__(self):
        self.allstars = []

    def create_s(self):
        rand_chance = random.randint(1, 20)
        if rand_chance == 1:
            star = Turtle("classic")
            star.setheading(270)
            star.shapesize(1)
            star.color("ghost white")
            star.penup()
            rand_x = random.randint(-200, 200)
            star.goto(rand_x, 300)
            self.allstars.append(star)

    def move_s(self):
        for star in self.allstars:
            star.forward(20)


class Bomb:

    def __init__(self):
        self.allbombs = []

    def create_b(self):
        rand_chance = random.randint(1, 10)
        if rand_chance == 1:
            bomb = Turtle("circle")
            bomb.setheading(270)
            bomb.shapesize(0.5)
            bomb.color("ghost white")
            bomb.penup()
            rand_x = random.randint(-200, 200)
            bomb.goto(rand_x, 300)
            self.allbombs.append(bomb)

    def move_b(self):
        for bomb in self.allbombs:
            bomb.forward(20)
