import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("TURTLE CROSS")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    # Detect when turtle hits car
    for each_car in car.all_cars:
        if each_car.distance(player) < 15:
            game_is_on = False
            score.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.level_increasing()
