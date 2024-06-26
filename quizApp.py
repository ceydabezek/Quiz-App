import tkinter as tk
from tkinter import messagebox
import random
import time

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        valid_answers = [choice[0] for choice in self.choices]
        if answer not in valid_answers:
            messagebox.showwarning("Warning", f"Invalid answer. Please choose one of the following: {', '.join(valid_answers)}")
            return False
        return self.answer == answer

class Quiz:
    def __init__(self, questions, time_limit=30):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0
        self.time_limit = time_limit
        self.root = tk.Tk()
        self.root.geometry("400x300")  # Pencere boyutunu ayarla
        self.setupWindow()

    def setupWindow(self):
        self.root.title("Quiz")
        self.questionLabel = tk.Label(self.root, text="")
        self.questionLabel.pack()

        self.choicesButtons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda i=i: self.answerQuestion(i))
            button.pack(fill=tk.BOTH, expand=True)
            self.choicesButtons.append(button)

    def getQuestion(self):
        return self.questions[self.questionIndex]  
    
    def displayQuestion(self):
        question = self.getQuestion()
        self.questionLabel.config(text=f"Question {self.questionIndex + 1}: {question.text}")

        for i in range(4):
            self.choicesButtons[i].config(text=f"{question.choices[i][0]}) {question.choices[i][1]}")

        self.start_time = time.time()

    def answerQuestion(self, choice):
        elapsed_time = time.time() - self.start_time

        if elapsed_time > self.time_limit:
            messagebox.showinfo("Time's Up", f"You took too long to answer. The correct answer is {self.questions[self.questionIndex].answer}")
        elif self.questions[self.questionIndex].checkAnswer(self.questions[self.questionIndex].choices[choice][0]):
            self.score += 1
            messagebox.showinfo("Correct", "Congratulations, you answered the question correctly.")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, you answered the question incorrectly. The correct answer is {self.questions[self.questionIndex].answer}")

        self.questionIndex += 1
        if self.questionIndex < len(self.questions):
            self.displayQuestion()
        else:
            self.displayScore()  

    def displayScore(self):
        messagebox.showinfo("Test Result", f"You answered correctly {self.score} questions out of {len(self.questions)}.\nYour score is {(self.score / len(self.questions)) * 100:.2f}%")
        self.root.destroy()

    def startQuiz(self):
        self.displayQuestion()
        
        self.root.mainloop()

q1 = Question("Which of the following is a correct way to create a list in Python?", 
              [("A", "list = {1, 2, 3}"), ("B", "list = (1, 2, 3)"), ("C", "list = [1, 2, 3]"), ("D", "list = <1, 2, 3>")], 
              "C")

q2 = Question("How do you start a comment in Python?", 
              [("A", "// This is a comment"), ("B", "<!-- This is a comment -->"), ("C", "# This is a comment"), ("D", "/* This is a comment */")], 
              "C")

q3 = Question("Which programming language is the most profitable?", 
              [("A", "Python"), ("B", "C#"), ("C", "Java"), ("D", "Dart")], 
              "A") 

questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.startQuiz()
