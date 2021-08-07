# Object state and instances

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

colors = ["red", "orange", "blue", "purple"]
# These objects can have different attributes and can be
# performing different methods at any one time
# In programming, is known as their state

leonardo = Turtle(shape="turtle")
leonardo.color("blue")
raphael = Turtle(shape="turtle")
raphael.color("red")
donatello = Turtle(shape="turtle")
donatello.color("purple")
michelangelo = Turtle(shape="turtle")
michelangelo.color("orange")

direction = {leonardo: [-230, -100, "blue", "Leonardo"],
             raphael: [-230, -50, "red", "Raphael"],
             donatello: [-230, 0, "purple", "Donatello"],
             michelangelo: [-230, 50, "orange", "Michelangelo"]}


for tmnt in direction.keys():
    x = direction[tmnt][0]
    y = direction[tmnt][1]
    tmnt.penup()
    tmnt.speed(5)
    tmnt.goto(x, y)

is_race_on = False

if user_bet:
    is_race_on = True

# turtle object is 40 x 40 object

while is_race_on:
    for turtle in direction.keys():
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The winner is {direction[turtle][2]} turtle named {direction[turtle][3]}! "
                      f"You got $100!")
            else:
                print(f"You've lost.... The winner is {direction[turtle][2]} turtle named {direction[turtle][3]}! "
                      f"Try again!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
