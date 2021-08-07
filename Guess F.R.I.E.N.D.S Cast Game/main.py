import pandas
import turtle
import time

guessed = []

data = pandas.read_csv('person.csv')
person_list = data.name.to_list()
xcor_list = data.x.to_list()
ycor_list = data.y.to_list()
gif_list = data.gif.to_list()

screen = turtle.Screen()
screen.title("F.R.I.E.N.D.S Quiz")
image = gif_list[0]
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
# def get_mouse_click(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click)


while len(guessed) < 12:

    answer = screen.textinput(title=f"Level {len(guessed) + 1}",
                              prompt="Who is this one?").title()

    for i in range(0, 12):

        if answer == person_list[i]:
            time.sleep(0.1)
            guessed.append(answer)
            if person_list[i] != "T":
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(int(xcor_list[i]), (int(ycor_list[i]) - 20))
                t.write(answer, move=False, align="center", font=("Arial", 12, "normal"))
                screen.addshape(gif_list[i + 1])
                turtle.shape(gif_list[i + 1])
                t.clear()
                screen.update()
                answer = screen.textinput(title=f"Level {len(guessed) + 1}",
                                          prompt="Who is this one?").title()
            else:
                t = turtle.Turtle()
                t2 = turtle.Turtle()
                t.clear()
                t2.clear()
                screen.addshape('friends.gif')
                turtle.shape('friends.gif')
                t.hideturtle()
                t.penup()
                t2.hideturtle()
                t2.penup()
                t.goto(5, 210)
                t2.goto(5, -240)
                t.write(f"YOU WIN!!!\nSCORE = 12/12", move=False, align="center", font=("Arial", 15, "bold"))
                t2.write("Thanks for playing!", move=False, align="center", font=("Arial", 15, "bold"))
                screen.update()
                screen.exitonclick()

    if answer == "Finish":
        missing_cast = []
        for i in person_list:
            if i not in guessed:
                missing_cast.append(i)
        new_data = pandas.DataFrame(missing_cast).to_csv("Missed_FRIENDS_Cast.csv")
        break
