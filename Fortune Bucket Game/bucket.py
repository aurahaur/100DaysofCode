from turtle import Turtle


class Bucket(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0, -200)
        self.color("chocolate4")
        self.begin_fill()
        self.shape("square")
        self.shapesize(2)
        self.end_fill()

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
