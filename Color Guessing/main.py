import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Color Guessing")
root.geometry("600x300")
root.resizable(0, 0)
root.iconbitmap("color.ico")

#  Colors Data
colors_data = {
    "Purple": "blue",
    "Yellow": "red",
    "black": "green",
    "Green": "orange",
    "Brown": "black",
    "Grey": "white"
}

list_quest = [x for x in colors_data.keys()]
list_ans = [x for x in colors_data.values()]

score = 0
timeleft = 30


def countdown():
    global score, timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text=f"Time Left: {str(timeleft)}")
        timeLabel.after(1000, countdown)
    if timeleft == 0:
        left_frame.destroy()
        right_frame.destroy()
        win = Label(text=f"Time's up!\nCongratulations! Your score is {score}", font=("Archery", 16))
        win.pack()


def check_answer():
    global score, timeleft
    user_answer = answer_entry.get().lower()

    if timeleft == 30:
        countdown()

    if timeleft > 0:
        if user_answer == "Enter Your Answer Here" or len(user_answer) == 0:
            tkinter.messagebox.showerror("Error", "You could not leave the field empty!")
        if user_answer == list_ans[0]:
            score += 1
        answer_entry.delete(0, END)

        random.shuffle(list_quest)
        random.shuffle(list_ans)

        color_guess.config(fg=list_ans[0], text=list_quest[1])
        score_label.config(text=f"Score: {score}")


left_frame = Frame(root)
left_frame.pack(side=LEFT)

right_frame = Frame(root)
right_frame.pack(side=RIGHT)

color_png = PhotoImage(file="color.png")
color_label = ttk.Label(left_frame, image=color_png, padding=5)
color_label.grid(row=1, column=0)

timeLabel = Label(right_frame, text=f"Time Left: {str(timeleft)}", font=("Helvetica", 12, "bold"))
timeLabel.grid(row=0, column=2, padx=100)

color_guess = Label(right_frame, text=list_quest[0], fg=list_ans[0], font=("Twelve Ton Sushi", 20, "bold"))
color_guess.grid(row=1, column=2, padx=100)

color_question = Label(right_frame, text="What color is that?", fg="black", font=("Arial", 12, "italic"))
color_question.grid(row=2, column=2, padx=100, pady=5)

answer_entry = Entry(right_frame, font=("Arial", 10))
answer_entry.grid(row=3, column=2, padx=100, pady=5)
answer_entry.insert(0, "Enter Your Answer Here")
answer_entry.configure(state=DISABLED)


def on_click_ans(event):
    answer_entry.configure(state=NORMAL)
    answer_entry.delete(0, END)
    answer_entry.unbind('<Button-1>', on_click_id)


on_click_id = answer_entry.bind('<Button-1>', on_click_ans)

ok_button = Button(right_frame, text="OK!", width=10, command=check_answer)
ok_button.grid(row=4, column=2, padx=100, pady=20)

score_label = Label(right_frame, text=f"Score: {score}")
score_label.grid(row=5, column=2, padx=100, pady=10)
root.mainloop()
