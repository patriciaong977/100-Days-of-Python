# Write a for loop to iterate over the question_data.
# Create a Question object from each entry in question_data.
# Append each Question object to the question_bank.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_Bank = []

for q in question_data:
    q_Question = q["question"]
    q_Answer = q["correct_answer"]

    create_Question = Question(q_Question, q_Answer)
    question_Bank.append(create_Question)


quiz = QuizBrain(question_Bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_Bank)}") # quiz.question_number
