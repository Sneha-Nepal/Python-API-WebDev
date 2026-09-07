# Quiz Game

Quiz Game is a simple game made by using Object-Oriented Programming (OOP). This project was built to master modular design and object-oriented syntax.

## Update

* Added a **Tkinter GUI** with a question display, score label, and True/False buttons.
* Added instant visual feedback by changing the question background color based on the answer.
* Added automatic progression to the next question after answering.
* Integrated the **Open Trivia Database API** to fetch questions dynamically.
* Added API request parameters for quiz amount, category, difficulty, and question type.
* Added HTML entity decoding to display API questions correctly.

## Features

* **Questioning:** Prompts the user with questions sequentially and accepts user input for answers.
* **Instant Feedback:** Validates answers immediately, updates the total score, and displays real-time progress after each question.
* **Dynamic Game Loop:** Automatically checks if questions remain in the bank and stops execution when all questions are answered.

## OOP Integration (Object-Oriented Programming)

* **Separation of Data Models:** The code is divided across separate files (`question_model.py`, `quiz_brain.py`, and `main.py`) to keep data models separated from execution logic.
* **Logic Management (`QuizBrain` Class):** Encapsulates the entire game attributes (current score, current question number, question list) and behavior (`next_question()`, `check_answer()`, `still_has_questions()`).
* **Object Instantiation:** Transforms raw dictionary data into a clean `question_bank` list containing initialized `Question` objects.

## Concepts Learned & Applied

* **Classes & Constructors:** Defining class attributes using `__init__()` and instantiating objects.
* **Control Flow & Iteration:** Using `while` loops driven by class methods (`still_has_questions()`) to control program flow.
* **List Comprehension:** Constructing lists of objects cleanly in a single readable line.
