from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#CD533B"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("AniManga Quiz")
        self.window.geometry("500x500")
        self.window.resizable(0, 0)
        self.window.configure(bg=THEME_COLOR)
        self.score = Label(text="Score: 0", font=("Arial", 12), bg=THEME_COLOR, fg="white")
        self.score.place(x=350, y=20)
        self.canvas = Canvas(width=340, height=200, highlightthickness=0)
        self.question_text = self.canvas.create_text(170, 100, text="Questions appear here", fill="black",
                                                     width=250, font=("Arial", 16, "italic"))
        self.canvas.config(bg="white")
        self.canvas.place(x=80, y=100)
        self.false = PhotoImage(file="images/false.png")
        self.true = PhotoImage(file="images/true.png")
        self.false_button = Button(image=self.false, highlightthickness=0, command=self.false_pressed)
        self.true_button = Button(image=self.true, highlightthickness=0, command=self.true_pressed)
        self.false_button.place(x=100, y=350)
        self.true_button.place(x=300, y=350)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")

        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)
