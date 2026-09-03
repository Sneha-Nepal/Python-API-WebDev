# Quiz Game

Quiz Game is a simple game made by using Object-Oriented Programming (OOP). This project was built to master modular design and object-oriented syntax.

## Features

* **Questioning:** Prompts the user with questions sequentially and accepts user input for answers.
* **Instant Feedback:** Validates answers immediately, updates the total score, and displays real-time progress after each question.
* **Dynamic Game Loop:** Automatically checks if questions remain in the bank and stops execution when all questions are answered.

## Uniquness

To distinct it with normal tutorials, I have added a `time` feature by using `import time`.

* **Time Tracking:** The game records the time when the question is displayed and when it is answered. Hence, the time difference is calculated.
* **Bonus Score:** The game awards bonus score for question answered below 10 seconds. Correct answers taking longer than 10 seconds yield the standard 1 point.

## OOP Integration (Object-Oriented Programming)

* **Separation of Data Models:** The code is divided across separate files (`question_model.py`, `quiz_brain.py`, and `main.py`) to keep data models separated from execution logic.
* **Logic Management (`QuizBrain` Class):** Encapsulates the entire game attributes (current score, current question number, question list) and behavior (`next_question()`, `check_answer()`, `still_has_questions()`).
* **Object Instantiation:** Transforms raw dictionary data into a clean `question_bank` list containing initialized `Question` objects.

## Concepts Learned & Applied

* **Classes & Constructors:** Defining class attributes using `__init__()` and instantiating objects.
* **Control Flow & Iteration:** Using `while` loops driven by class methods (`still_has_questions()`) to control program flow.
* **List Comprehension:** Constructing lists of objects cleanly in a single readable line.
