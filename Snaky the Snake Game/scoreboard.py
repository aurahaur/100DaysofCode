from turtle import Turtle

alignment = "center"
font = ("Castellar", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data_snake.txt') as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Your score = {self.score} | High Score = {self.highscore}", False, alignment, font)

    def plus_score(self):
        self.score += 1
        self.clear()
        self.write(f"Your score = {self.score} | High Score = {self.highscore}", False, alignment, font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data_snake.txt', mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f"Your score = {self.score} | High Score = {self.highscore}", False, alignment, font)

