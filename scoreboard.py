from turtle import Turtle

alignment = "center"
font = ("Castellar", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Your score = {self.score}", False, alignment, font)

    def plus_score(self):
        self.score += 1
        self.clear()
        self.write(f"Your score = {self.score}", False, alignment, font)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", False, "center", ("Castellar", 15, "bold"))
