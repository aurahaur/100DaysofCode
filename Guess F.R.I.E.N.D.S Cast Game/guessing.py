from turtle import Turtle, Screen
import pandas

data = pandas.read_csv('person.csv')
person_list = data.name.to_list()
xcor_list = data.x.to_list()
ycor_list = data.y.to_list()
gif_list = data.gif.to_list()
screen = Screen()


class Person(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def guessing(self, num_list, answer):
        self.goto(int(xcor_list[num_list]), int(ycor_list[num_list] - 20))
        self.write(answer, move=False, align="center", font=("Arial", 12, "normal"))
        screen.addshape(gif_list[num_list + 1])
        self.shape(gif_list[num_list + 1])
        self.clear()
        screen.update()