# Create a class called QuizBrain.
# Write an __init__() method.
# Initialize the question_number to 0.
# Initialize the question_list to an input.

# Retrieve the item at the current question_number from the question_list.
# Use the input() function to show the user the Question text and ask for the user's answer.

# Create method called still_has_questions().
# Return a boolean depending on the value of question_number.
# Use the while loop to show the next question until the end.

# Add a score attribute.

class QuizBrain:

    def __init__(self, question_list):
        self.q_num = 0
        self.q_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.q_num < len(self.q_list)


    def next_question(self):
        curr_q = self.q_list[self.q_num]
        self.q_num += 1
        user_answer = input(f"Q.{self.q_num}: {curr_q.text} (True/False): ")
        self.check_answer(user_answer, curr_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.q_num}")
        print ("\n")
