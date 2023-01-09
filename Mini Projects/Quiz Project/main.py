# Import
from question_model import Question
from data import question_data

# Write a for loop to iterate over the question_data.
# Create a Question object from each entry in question_data.
# Append each Question object to the question_bank.

questionList = []

for q in question_data:
    q_Question = q["text"]
    q_Answer = q["answer"]

    create_Question = Question(q_Question, q_Answer)
    questionList.append(create_Question)
