from turtle import Turtle

alignment = "left"
font = ("Algerian", 30, "normal")


class Scoring(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", False, alignment, font)
        self.goto(100, 250)
        self.write(f"{self.r_score}", False, alignment, font)

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()
