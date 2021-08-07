from turtle import Turtle

FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-200, 200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def score_increasing(self):
        self.score += 1
        self.update_score()

    def score_decreasing(self):
        self.score -= 1
        self.update_score()

    def win(self):
        self.goto(0, 0)
        self.write("YOU WIN!!!")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!")