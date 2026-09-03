import time
import html 

# Unescape the question recieved from the API. 
# The quoations and few other things were not clear and contained different symbols so unescaping was necessary.
# Asks the question, checks the answer, checking if the quiz has ended.

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Checks if questions are left in the question_bank"""
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        """Provides the next question to move forward with the game"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        start_time = time.time()
        q_text = html.unescape(current_question.text)
        user_answer = input(f"Q.{self.question_number}. {q_text} (True/False)? : ")
        end_time = time.time()
        elapsed = round(end_time - start_time, 1)
        self.check_answer(user_answer, current_question.answer, elapsed)

    def check_answer(self, user_answer, current_answer, e_time):
        """Checks the answer and tracks the score along with the time"""
        print(f"You took {e_time} seconds")
        if user_answer.lower() == current_answer.lower():
            if e_time <= 10:
                print("Your time was less than 10. Score increased by TWO!")
                self.score += 2
            else:
                print("Score increased by ONE.")
                self.score += 1
        else:
            print("Wrong answer. No points for this question!")

        print(f"Score : {self.score}")
        print(f"Question : {self.question_number}")
        print("\n")
