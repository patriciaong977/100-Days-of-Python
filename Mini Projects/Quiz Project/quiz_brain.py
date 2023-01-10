# Create a class called QuizBrain.
# Write an __init__() method.
# Initialize the question_number to 0.
# Initialize the question_list to an input.

# Retrieve the item at the current question_number from the question_list.
# Use the input() function to show the user the Question text and ask for the user's answer.

# Create method called still_has_questions().
# Return a boolean depending on the value of question_number.
# Use the while loop to show the next question until the end.

class QuizBrain:

    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list

    def still_has_questions(self):
        while self.q_num < len(self.q_list):
            return True

    def next_question(self):
        curr_q = self.q_list[self.q_num]
        self.q_num += 1
        input(f"Q.{self.q_num}: {curr_q.text} (True/False): ")
