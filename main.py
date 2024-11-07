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
# Function to get quiz questions from the selected table
def get_quiz_questions(table_name):
    conn = sqlite3.connect('programming_quiz.db')
    cursor = conn.cursor()

    # Enclose the table name in double quotes to avoid syntax errors if it starts with a number
    cursor.execute(f'SELECT * FROM "{table_name}"')
    
    questions = cursor.fetchall()
    conn.close()
    print(f"Retrieved {len(questions)} questions from {table_name}")
    return questions


# Function to display the quiz window
def display_quiz(table_name):
    quiz_window = tk.Toplevel(root)
    quiz_window.title(f"Quiz for {table_name}")
    quiz_window.geometry("800x600")

    questions = get_quiz_questions(table_name)
    current_question = [0]  # To track current question index
    score = [0]  # To track the user's score

    if not questions:
        messagebox.showerror("Error", "No questions found for this table.")
        quiz_window.destroy()
        return

    # Function to display the next question
    def show_question():
        if current_question[0] < len(questions):
            q_id, question, option1, option2, option3, option4, correct_answer = questions[current_question[0]]
            print(f"Displaying question {current_question[0] + 1}: {question}")
            question_label.config(text=question)
            radio_var.set(None)  # Reset radio button selection
            radio_button1.config(text=option1, value=option1)
            radio_button2.config(text=option2, value=option2)
            radio_button3.config(text=option3, value=option3)
            radio_button4.config(text=option4, value=option4)
        else:
            # End of quiz
            messagebox.showinfo("Quiz Complete", f"You've completed the quiz! Your score: {score[0]}/{len(questions)}")
            quiz_window.destroy()

    # Function to handle answer submission
    def submit_answer():
        selected_option = radio_var.get()
        if not selected_option:
            messagebox.showwarning("No selection", "Please select an answer before submitting!")
            return
        
        correct_option = questions[current_question[0]][6]  # Get correct answer
        if selected_option == correct_option:
            score[0] += 1
            messagebox.showinfo("Correct", "Correct!")
        else:
            messagebox.showinfo("Incorrect", f"Incorrect! The correct answer was: {correct_option}")
        
        current_question[0] += 1  # Move to the next question
        show_question()  # Show the next question

    # GUI elements inside quiz window
    question_label = tk.Label(quiz_window, text="", wraplength=600)
    question_label.pack(pady=20)

    radio_var = tk.StringVar()
    radio_button1 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    radio_button2 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    radio_button3 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")
    radio_button4 = tk.Radiobutton(quiz_window, text="", variable=radio_var, value="")

    radio_button1.pack(pady=5)
    radio_button2.pack(pady=5)
    radio_button3.pack(pady=5)
    radio_button4.pack(pady=5)

    submit_button = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_button.pack(pady=20)

    # Start by showing the first question
    quiz_window.update_idletasks()  # Force the window to render all components
    show_question()

# Main window
root = tk.Tk()
root.title("Quiz Bowl - Select Table")
root.geometry("800x600")

tables = get_table_names()

table_listbox = tk.Listbox(root)
for table in tables:
    table_listbox.insert(tk.END, table)

table_listbox.pack(pady=20)

def start_quiz():
    selected_table = table_listbox.get(tk.ACTIVE)
    if selected_table:
        display_quiz(selected_table)

start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack(pady=20)

root.mainloop()
