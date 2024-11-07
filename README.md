# QA3.2
# Quarterly-Assessment-3

This project is part of the Quarterly Assessment for the DS 3850 course. It is a Python-based quiz application using a graphical user interface (GUI) built with Tkinter. The application allows users to select a quiz category and answer multiple-choice questions from a database. The user receives immediate feedback after answering the questions. They will be told if their answer was correct, or the correct answer if they missed the question. The user's score is calculated based on their responses, and which the user receives at the end of the quiz. 

Features
1. Multiple-choice quiz with 10 questions for each course
2. Dynamic question loading from a SQLite database.
3. Score calculation and feedback after quiz completion.

Five categories available for quizzes:
1. DS 4220
2. DS 4210
3. DS 3850
4. ECON 4990
5. FIN 3210

Project Structure
1. main.py: The main file that runs the GUI and interacts with the database.
2. addData.py: The database file where questions and answers are stored.
3. programming_quiz.db: The SQLite database containing the quiz questions for each category.
4. README.md: Instructions and details about the project.