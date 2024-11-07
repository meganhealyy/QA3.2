import sqlite3
import tkinter as tk
from tkinter import messagebox

# Function to get table names from the database
def get_table_names():
    conn = sqlite3.connect('programming_quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()
    conn.close()
    return [table[0] for table in tables]

# Function to get quiz questions from the selected table
def get_quiz_questions(table_name):
    conn = sqlite3.connect('programming_quiz.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    questions = cursor.fetchall()
    conn.close()
    return questions

# Function to display the quiz window
def display_quiz(table_name):
    quiz_window = tk.Toplevel(root)
    quiz_window.title(f"Quiz for {table_name}")
    questions = get_quiz_questions(table_name)
    current_question = [0]  # To track current question index

    def show_question():
        if current_question[0] < len(questions):
            q_id, question, option1, option2, option3, option4, correct_answer = questions[current_question[0]]
            question_label.config(text=question)
            radio_var.set(None)  # Reset selection
            radio_button1.config(text=option1)
            radio_button2.config(text=option2)
            radio_button3.config(text=option3)
            radio_button4.config(text=option4)
        else:
            messagebox.showinfo("End of Quiz", "You have answered all questions!")
            quiz_window.destroy()

    def submit_answer():
        selected_option = radio_var.get()
        correct_option = questions[current_question[0]][6]  # correct_answer from tuple
        if selected_option == correct_option:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer was: {correct_option}")
        current_question[0] += 1
        show_question()

    # GUI elements
    question_label = tk.Label(quiz_window, text="")
    question_label.pack()

    radio_var = tk.StringVar()
    radio_button1 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="option1")
    radio_button2 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="option2")
    radio_button3 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="option3")
    radio_button4 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="option4")

    radio_button1.pack()
    radio_button2.pack()
    radio_button3.pack()
    radio_button4.pack()

    submit_button = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_button.pack()

    show_question()  # Show the first question

# Step 2: Create the Main Window and Show the List of Tables
root = tk.Tk()
root.title("Quiz Bowl - Select Table")

tables = get_table_names()

table_listbox = tk.Listbox(root)
for table in tables:
    table_listbox.insert(tk.END, table)

table_listbox.pack()

def start_quiz():
    selected_table = table_listbox.get(tk.ACTIVE)
    if selected_table:
        display_quiz(selected_table)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

root.mainloop()
