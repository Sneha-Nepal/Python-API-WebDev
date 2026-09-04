from tkinter import *
from quiz_brain import QuizBrain

THEME = "#375362"
TXT_FONT = ("Arial", 16, "italic")
WHITE = "#FFFFFF"
GREEN = "#2ecc71"
RED = "#e74c3c"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Quiz Python")
        self.screen.config(padx=20, pady=20, bg=THEME)

        # Score Label
        self.score_label = Label(self.screen, text="Score: 0", bg=THEME, fg=WHITE, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1, pady=(0, 20))

        # Canvas for Question Text
        self.canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, fill=THEME, font=TXT_FONT, 
            text="Question text will apear here")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # True Button
        self.T_btn = Button(self.screen, text="True", font=("Arial", 16, "bold"), fg=WHITE, bg=GREEN, 
            activebackground=GREEN, activeforeground=WHITE, width=8, height=2, bd=0)
        self.T_btn.grid(row=2, column=0, padx=10)

        # False Button
        self.F_btn = Button(self.screen, text="False", font=("Arial", 16, "bold"), fg=WHITE, bg=RED, 
            activebackground="#c0392b", activeforeground=WHITE, width=8, height=2, bd=0)
        self.F_btn.grid(row=2, column=1, padx=10)

        self.get_next_question()

        self.screen.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
