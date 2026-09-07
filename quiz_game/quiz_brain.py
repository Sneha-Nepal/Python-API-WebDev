import html 

# Unescape the question recieved from the API. 
# The quoations and few other things were not clear and contained different symbols so unescaping was necessary.
# Asks the question, checks the answer, checking if the quiz has ended.

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = self.question_list[self.question_number]

    def still_has_questions(self):
        """Checks if questions are left in the question_bank"""
        if self.question_number >= len(self.question_list):
            return False
        return True

    def next_question(self):
        """Provides the next question to move forward with the game"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}. {q_text}"

    def check_answer(self, user_answer):
        """Checks the answer and tracks the score"""
        current_answer = self.current_question.answer
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            return True
        else:
            return False
