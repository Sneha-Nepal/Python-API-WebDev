from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI

# Storing the question objects in the question_bank as a list of objects
question_bank = [(Question(question["question"], question["correct_answer"])) for question in question_data]

# Getting the questions
quiz = QuizBrain(question_bank)
q_UI = QuizUI(quiz)

# Storing score and question_number attributes.
score = quiz.score
q_number = quiz.question_number

print("You have completed the Quiz!!")
print(f"Your final score is {score} / {q_number}.")
