from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, padx = 20, pady = 20 )

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="Question Text", 
            fill = THEME_COLOR, 
            font=("Ariel", 20, "italic"),
            width = 280,
        )
        self.canvas.pack()
        self.canvas.grid(row = 1, column = 0, columnspan= 2, pady=50)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(row = 0, column = 1)

        tb = PhotoImage(file="images/true.png")
        fb = PhotoImage(file="images/false.png")
        self.true_button = Button(image=tb, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row = 2, column=0)
        self.false_button = Button(image=fb, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row = 2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz.\nYour score was {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)