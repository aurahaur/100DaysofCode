from turtle import Screen
from bucket import Bucket
from star_bomb import Star, Bomb
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("midnight blue")
screen.setup(500, 500)
screen.title("Fortune Bucket")
screen.tracer(0)

bucket = Bucket()
star = Star()
bomb = Bomb()
score = Scoreboard()

screen.listen()

screen.onkey(bucket.move_left, "Left")
screen.onkey(bucket.move_right, "Right")

bomb_max = 0
star_max = 0

while True:
    time.sleep(0.1)
    star.create_s()
    star.move_s()
    bomb.create_b()
    bomb.move_b()
    screen.update()

    # Detect if square bucket hits a star and bomb
    for each_star in star.allstars:
        if each_star.distance(bucket) < 10:
            star_max += 1
            score.score_increasing()
            each_star.hideturtle()

    for each_bomb in bomb.allbombs:
        if each_bomb.distance(bucket) < 10:
            bomb_max += 1
            score.score_decreasing()
            each_bomb.hideturtle()

    # Detect if player wins
    if star_max == 10:
        score.win()
        break

    elif bomb_max == 3:
        score.game_over()
        break

screen.exitonclick()
