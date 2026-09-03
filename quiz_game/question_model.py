# Creates the quiz question models. Generates questions.

class Question:
    def __init__(self, text, answer):
        """Constructor method with text and answer attributes"""
        self.text = text
        self.answer = answer
