import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Gameplay")
image = 'us.gif'
screen.addshape(image)
turtle.shape(image)

guessed = []
# print(answer_state)
data = pandas.read_csv('50-states.csv')
state = data.state.to_list()


while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 States Correct",
                                    prompt="What's the state's name?").title()
    # if answer_state is one of the states in all the states of csv file
    if answer_state in state:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # state_data.state.item()

    if answer_state == "Exit":
        missing_states = []
        for i in state:
            if i not in guessed:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_Learn.csv")
        break
